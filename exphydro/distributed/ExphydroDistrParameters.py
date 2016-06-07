#!/usr/bin/env python

# Programmer(s): Sopan Patil.
# This file is part of the 'exphydro.distributed.type1' package.

from exphydro.lumped import ExphydroParameters


######################################################################

class ExphydroDistrParameters(object):

    def __init__(self, npixels):

        """ Each parameter set contains npixel number of realisations
        of the lumped EXP-HYDRO model parameters as well as default
        values of the objective function.
        """

        self.pixels = npixels  # Number of pixels
        self.objval = -9999  # This is the objective function value

        # The statement below creates npixel instances of the
        # lumped EXP-HYDRO model parameters
        self.params = [ExphydroParameters() for j in range(npixels)]

    # ----------------------------------------------------------------

    def updateparameters(self, para1, para2, w):

        """ This function is used for PSO algorithm.
        """

        for i in range(self.pixels):
            self.params[i].updateparameters(para1.params[i], para2.params[i], w)

######################################################################
