#!/usr/bin/env python

# Programmer(s): Sopan Patil.
# This file is part of the 'exphydro.lumped' package.

import numpy
from hydroutils import OdeSolver


######################################################################

class ExphydroModel(object):

    """ An EXP-HYDRO bucket has its own climate inputs.

    It also has the properties of storage (both soil
    and snow), stream discharge (qsim), snowmelt (melt) and
    evapotranspiration (et)
    """

    def __init__(self, p, pet, t):

        """ This method is used to initialise, i.e., create an instance of the ExphydroModel class.

        Syntax: ExphydroModel(p, pet, t)

        Args:
            (1) p: Daily precipitation time-series (mm/day)
            (2) pet: Daily potential evapotranspiration time-series (mm/day)
            (3) t: Daily mean air temperature time-series (deg C)

        """

        # Below are the climate inputs
        self.P = p  # Daily precipitation (mm/day)
        self.PET = pet  # Daily PET (mm/day)
        self.T = t  # Daily mean air temperature (deg C)

        self.timespan = self.P.shape[0]  # Time length of the simulation period

        # Below are the state and flux variables of EXP-HYDRO
        #  All of them are initialised to zero
        self.storage = numpy.zeros(2)  # Storage of soil and snow buckets (mm)
        self.qsim = numpy.zeros(self.timespan)  # Simulated streamflow (mm/day)
        self.et = numpy.zeros(self.timespan)  # Simulated ET (mm/day)
        self.melt = numpy.zeros(self.timespan)  # Simulated snowmelt (mm/day)

    # ----------------------------------------------------------------

    def waterbalance(self, t, s, para):

        """ This method provides the right hand side of the dS/dt equations."""

        # EXP-HYDRO parameter values from object para
        f = para.f.value
        ddf = para.ddf.value
        smax = para.smax.value
        qmax = para.qmax.value
        mint = para.mint.value
        maxt = para.maxt.value

        # The line below ensures that the time step of input and output variables is always an integer.
        # ODE solvers can take fractional time steps, for which input data does not exist.
        tt = min(round(t), self.timespan-1)

        # NOTE: The min condition in above line is very important and is needed when the ODE solver
        # jumps to a time-step that is beyond the time-series length.

        # Loading the input data for current time step
        p = self.P[tt]
        te = self.T[tt]
        pet = self.PET[tt]

        # Partitioning precipitation into rain and snow
        [ps, pr] = self.rainsnowpartition(p, te, mint)

        # Snow bucket
        m = self.snowbucket(s[0], te, ddf, maxt)

        # Soil bucket
        [et, qsub, qsurf] = self.soilbucket(s[1], pet, f, smax, qmax)

        # Water balance equations
        ds1 = ps - m
        ds2 = pr + m - et - qsub - qsurf

        ds = numpy.array([ds1, ds2])

        # Writing the flux calculations into output variables for the
        # current time step
        self.qsim[tt] = qsub + qsurf
        self.et[tt] = et
        self.melt[tt] = m

        return ds

    # ----------------------------------------------------------------

    @staticmethod
    def rainsnowpartition(p, t, mint):

        """ EXP-HYDRO equations to partition incoming precipitation
        into rain or snow."""

        if t < mint:
            psnow = p
            prain = 0
        else:
            psnow = 0
            prain = p

        return [psnow, prain]

    # ----------------------------------------------------------------

    @staticmethod
    def snowbucket(s, t, ddf, maxt):

        """ EXP-HYDRO equations for the snow bucket."""

        if t > maxt:
            if s > 0:
                melt = min(s, ddf*(t - maxt))
            else:
                melt = 0
        else:
            melt = 0

        return melt

    # ----------------------------------------------------------------

    @staticmethod
    def soilbucket(s, pet, f, smax, qmax):

        """ EXP-HYDRO equations for the soil bucket."""

        if s < 0:
            et = 0
            qsub = 0
            qsurf = 0
        elif s > smax:
            et = pet
            qsub = qmax
            qsurf = s - smax
        else:
            qsub = qmax * numpy.exp(-f * (smax - s))
            qsurf = 0
            et = pet * (s / smax)

        return [et, qsub, qsurf]

    # ----------------------------------------------------------------

    def simulate(self, para):

        """ This method performs the integration of dS/dt equations
        over the entire simulation time period
        """

        # Solving the ODE. To check which ODE solvers are available to use,
        # please check OdeSolver.py in bangormodeltools
        OdeSolver.solve_rk4(self.waterbalance, self.storage, para, tlength=self.timespan)
        return self.qsim

######################################################################
