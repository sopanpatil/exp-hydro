#!/usr/bin/env python

# Programmer(s): Sopan Patil.
# This file is part of the 'exphydro.distributed' package.

from exphydro.utils import Parameter
from exphydro.lumped import ExphydroParameters


######################################################################

class ExphydroDistrParameters(object):

    def __init__(self, npixels):

        """ Each parameter set contains npixel number of realisations
        of the lumped EXP-HYDRO model parameters as well as default
        values of the objective function.
        """

        self.pixels = npixels # Number of pixels
        self.objval = -9999  # This is the objective function value

        # The statement below creates npixel instances of the
        # lumped EXP-HYDRO model parameters
        self.params = [ExphydroParameters() for j in range(npixels)]

    # ----------------------------------------------------------------

    def updateparameters(self, para1, para2, w):

        """ This function is used for PSO algorithm.
            Each parameter in the model has to do the following
            two things:
            (1) Update its velocity
            (2) Update its value
        """

        # Update parameter velocities

        for i in range(self.pixels):
            self.params[i].f.updatevelocity(para1.params[i].f, para2.params[i].f, w)
            self.params[i].ddf.updatevelocity(para1.params[i].ddf, para2.params[i].ddf, w)
            self.params[i].smax.updatevelocity(para1.params[i].smax, para2.params[i].smax, w)
            self.params[i].qmax.updatevelocity(para1.params[i].qmax, para2.params[i].qmax, w)
            self.params[i].mint.updatevelocity(para1.params[i].mint, para2.params[i].mint, w)
            self.params[i].maxt.updatevelocity(para1.params[i].maxt, para2.params[i].maxt, w)

            # Update parameter values
            self.params[i].f.updatevalue()
            self.params[i].ddf.updatevalue()
            self.params[i].smax.updatevalue()
            self.params[i].qmax.updatevalue()
            self.params[i].mint.updatevalue()
            self.params[i].maxt.updatevalue()

######################################################################
