#!/usr/bin/env python

# Programmer(s): Sopan Patil.
# This file is part of the 'hydroutils' package.

import numpy


######################################################################

class Parameter(object):

    """ The 'Parameter' class defines the basic properties of a parameter, such as
    its upper bound, lower bound, numeric value, and velocity (in case of PSO).
    """

    def __init__(self, lb, ub):

        """ This method is used to create an instance of the Parameter class.

        Syntax: Parameter(lb,ub)

        Args:
            (1) lb: Lower bound value of the parameter.

            (2) ub: Upper bound value of the parameter.
        """

        self.lb = lb  # Lower bound of a parameter
        self.ub = ub  # Upper bound of a parameter
        self.value = numpy.random.uniform(lb, ub)  # Random sampling of parameter value
        self.velocity = 0  # Velocity of a parameter (used for PSO algorithm)

    # ----------------------------------------------------------------

    def updatevelocity(self, param1, param2, w):

        """ This method is used by the PSO algorithm."""

        x = numpy.random.uniform(0, 1)
        y = numpy.random.uniform(0, 1)
        c1 = 2
        c2 = 2

        # Update the parameter velocity
        self.velocity = w*self.velocity + c1*x*(param1.value - self.value) + c2*y*(param2.value - self.value)

    # ----------------------------------------------------------------

    def updatevalue(self):

        """ This method is used by the PSO algorithm."""

        sf = 0.9  # This is a safety factor

        if (self.value + self.velocity) < self.lb:
            self.velocity = sf*(self.lb - self.value)
        if (self.value + self.velocity) > self.ub:
            self.velocity = sf*(self.ub - self.value)

        # Update the parameter value
        self.value += self.velocity

######################################################################
