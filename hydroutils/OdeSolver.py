#!/usr/bin/env python

# Programmer(s): Sopan Patil.
# This file is part of the 'hydroutils' package.

import numpy
from scipy import integrate
import warnings


warnings.filterwarnings("ignore")

######################################################################


class OdeSolver(object):

    """ The 'OdeSolver' class contains the method for solving a system of
    Ordinary Differential Equations.
    """

    @staticmethod
    def solve_rk45(userfunction, initstate, userpara, tlength):

        """ This method performs the integration of the user provided function
        over the specified simulation time period.
        The ODE solver used is Runge-Kutta 4-5th order with Dormand-Prince corrector.

        Args:
            (1) userfunction: Function that provides the right hand side equations of the ODE system
            of the user's model.

            (2) initstate: Initial values of the state variables in the ODE system.

            (3) userpara: Parameter set of the user's model.

            (4) tlength: time length of the model simulation period.

        """

        solver = integrate.ode(userfunction)
        solver.set_integrator('dopri5', atol=1e-6, rtol=1e-3)
        solver.set_initial_value(initstate, 0.0)
        solver.set_f_params(userpara)

        while solver.successful() and solver.t < tlength:
            solver.integrate(solver.t+1)

# ---------------------------------------------------------------------------------

    @staticmethod
    def solve_rk4(f, x0, para, tlength):

        """ This method performs the integration of the user provided function
        over the specified simulation time period.
        The ODE solver used in Runge-Kutta 4th order.

        Args:
            (1) f: Function that provides the right hand side equations of the ODE system

            (2) x0: Initial values of the state variables in the ODE system

            (3) para: Parameter set of the user's model

            (4) tlength: time length of the model simulation period.

        """
        t = numpy.arange(tlength)
        n = len(t)
        x = numpy.array([x0] * n)

        for i in range(n - 1):
            h = t[i+1] - t[i]
            k1 = h * f(t[i], x[i], para)
            k2 = h * f(t[i] + 0.5 * h, x[i] + 0.5 * k1, para)
            k3 = h * f(t[i] + 0.5 * h, x[i] + 0.5 * k2, para)
            k4 = h * f(t[i+1], x[i] + k3, para)
            x[i+1] = x[i] + (k1 + 2.0 * (k2 + k3) + k4) / 6.0


##################################################################################
