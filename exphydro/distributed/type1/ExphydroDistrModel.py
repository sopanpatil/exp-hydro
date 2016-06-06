#!/usr/bin/env python

# Programmer(s): Sopan Patil.
# This file is part of the 'exphydro.distributed.type1' package.

import numpy
from exphydro.lumped import ExphydroModel

######################################################################


class ExphydroDistrModel(object):

    def __init__(self, p, pet, t, npixels):

        """ This method is used to initialise, i.e., create an instance of the ExphydroDistrModel class.

        Syntax: ExphydroDistrModel(p, pet, t, npixels)

        Args:
            (1) p: Daily precipitation time-series (mm/day)
            (2) pet: Daily potential evapotranspiration time-series (mm/day)
            (3) t: Daily mean air temperature time-series (deg C)
            (4) npixels: Number of pixels in the catchment

        """

        # The statement below creates npixel instances of the lumped EXP-HYDRO model
        self.model = [ExphydroModel(p, pet, t) for j in range(npixels)]

        self.timespan = p.shape[0]  # Time length of the simulation period
        self.qsimtmp = numpy.zeros(self.timespan)  # Variable to temporarily store pixel's streamflow output
        self.qsim = numpy.zeros(self.timespan)  # Simulated streamflow (mm/day)

    # ----------------------------------------------------------------

    def simulate(self, para):

        """ This method simulates the EXP-HYDRO model over all pixels
        and provides a combined streamflow output.
        """

        npixels = para.pixels

        # In the for loop below, each instance of lumped EXP-HYDRO model
        # is run npixel times.
        for i in range(npixels):
            self.qsimtmp = self.model[i].simulate(para.params[i])

            # Averaging the Q output of all pixels
            if i == 0:
                self.qsim = self.qsimtmp
            else:
                self.qsim = (self.qsim + self.qsimtmp)*0.5

        return self.qsim

######################################################################
