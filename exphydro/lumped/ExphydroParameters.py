#!/usr/bin/env python

# Programmer(s): Sopan Patil.
# This file is part of the 'exphydro.lumped' package.

from exphydro.utils import Parameter


######################################################################

class ExphydroParameters(object):

    def __init__(self):

        """ Each parameter set contains a random realisation of all six
        EXP-HYDRO parameters as well as default values of Nash-Sutcliffe
        and Kling-Gupta efficiencies
        """

        self.f = Parameter(0, 0.1)
        self.smax = Parameter(100.0, 1500.0)
        self.qmax = Parameter(10.0, 50.0)
        self.ddf = Parameter(0.0, 5.0)
        self.mint = Parameter(-3.0, 0.0)
        self.maxt = Parameter(0.0, 3.0)

        self.objval = -9999  # This is the objective function value

    # ----------------------------------------------------------------

    def assignvalues(self, f, smax, qmax, ddf, mint, maxt):

        """ This method is used to manually assign parameter values,
        which are given by the user as input arguments.
        """

        self.f.value = f
        self.smax.value = smax
        self.qmax.value = qmax
        self.ddf.value = ddf
        self.mint.value = mint
        self.maxt.value = maxt

    # ----------------------------------------------------------------

    def updateparameters(self, param1, param2, w):

        """ This method is used for PSO algorithm.
            Each parameter in the model has to do the following
            two things:
            (1) Update its velocity
            (2) Update its value
        """

        # Update parameter velocities
        self.f.updatevelocity(param1.f, param2.f, w)
        self.ddf.updatevelocity(param1.ddf, param2.ddf, w)
        self.smax.updatevelocity(param1.smax, param2.smax, w)
        self.qmax.updatevelocity(param1.qmax, param2.qmax, w)
        self.mint.updatevelocity(param1.mint, param2.mint, w)
        self.maxt.updatevelocity(param1.maxt, param2.maxt, w)

        # Update parameter values
        self.f.updatevalue()
        self.ddf.updatevalue()
        self.smax.updatevalue()
        self.qmax.updatevalue()
        self.mint.updatevalue()
        self.maxt.updatevalue()

######################################################################
