#!/usr/bin/env python

# Programmer(s): Sopan Patil.
# This file is part of the 'exphydro.distributed.type3' package.

import numpy
from exphydro.lumped import ExphydroModel

######################################################################


class ExphydroDistrModel(object):

    def __init__(self, p, pet, t, nsubcats, subcatwts):

        """ This method is used to initialise, i.e., create an instance of the ExphydroDistrModel class.

        Syntax: ExphydroDistrModel(p, pet, t, npixels)

        Args:
            (1) p: Daily precipitation time-series (mm/day)
            (2) pet: Daily potential evapotranspiration time-series (mm/day)
            (3) t: Daily mean air temperature time-series (deg C)
            (4) nsubcats: Number of sub-catchments in the catchment
            (5) Relative weight of all sub-catchments (array). It is the proportion of area
            covered by each sub-catchment.  Sum of all array elements is 1.

        """

        # The statement below creates nsubcats instances of the lumped EXP-HYDRO model
        self.model = [ExphydroModel(p, pet, t) for j in range(nsubcats)]

        self.subcatwts = subcatwts  # Relative weight of each sub-catchment
        self.timespan = p.shape[0]  # Time length of the simulation period
        self.qsimtmp = numpy.zeros(self.timespan)  # Variable to temporarily store pixel's streamflow output
        self.qsim = numpy.zeros(self.timespan)  # Simulated streamflow (mm/day)

    # ----------------------------------------------------------------

    def simulate(self, para):

        """ This method simulates the EXP-HYDRO model over all sub-catchments
        and provides a combined streamflow output.
        """

        nsubcats = para.pixels

        # In the for loop below, each instance of lumped EXP-HYDRO model
        # is run nsubcats times.
        for i in range(nsubcats):
            self.qsimtmp = self.model[i].simulate(para.params[i])

            # Weight-based averaging the Q output of all sub-catchments
            if i == 0:
                self.qsim = self.subcatwts[i]*self.qsimtmp
            else:
                self.qsim = self.qsim + self.subcatwts[i]*self.qsimtmp

        return self.qsim

######################################################################
