#!/usr/bin/env python

# Programmer(s): Sopan Patil.
# This file is part of the 'exphydro.utils' package.

import numpy
import copy


######################################################################

class Calibration(object):

    """ The 'Calibration' class contains the following two methods for model calibration:
    (1) Particle Swarm Optimisation

    (2) Monte-Carlo Optimisation

    """

    @staticmethod
    def pso_maximise(model, params, obsdata, objf, calperiods_obs, calperiods_sim):

        """ This method optimises a user provided model by maximising the user provided
        objective function with the Particle Swarm Optimisation algorithm.

        Args:
            (1) model: Instance of the user provided model.

            (2) params: List of the instances of user provided model parameter sets.

            (3) obsdata: Time-series of the observed data (that will be compared with simulated data).

            (4) objf: Method from the ObjectiveFunction class specifying the objective function.

            (5) calperiods_obs: Two element array (or list) specifying the index values of the start
                            and end data points of calibration period for the observed data.

            (6) calperiods_sim: Two element array (or list) specifying the index values of the start
                            and end data points of calibration period for the simulated data.

        """

        # PSO algorithm parameters
        npart = len(params)  # No. of particles in a PSO swarm
        niter = 50  # Maximum number of swarm iterations allowed
        ertol = 1e-3   # Error tolerance for considering no optimisation improvement
        maxiter = 5  # Maximum swarm iterations allowed with no optimisation improvement
        nstp = 0
        winit = 0.9
        wend = 0.4
        w = winit
        objmax = numpy.zeros(niter)

        paramsbst = copy.deepcopy(params)
        paramsmax = params[0]

        # Start PSO
        for j in range(niter):
            for i in range(npart):

                # Simulate the model
                simdata = model.simulate(params[i])

                # Calculate the objective function value of simulation
                params[i].objval = objf(obsdata[calperiods_obs[0]:calperiods_obs[1]+1],
                                        simdata[calperiods_sim[0]:calperiods_sim[1]+1])

                # If the particle has improved upon its own best objective function
                if params[i].objval > paramsbst[i].objval:
                    # copy parameter set
                    paramsbst[i] = copy.deepcopy(params[i])

                # If the particle has improved upon entire swarm's objective function
                if params[i].objval > paramsmax.objval:
                    # copy parameter set
                    paramsmax = copy.deepcopy(params[i])

                # Update the parameter values
                params[i].updateparameters(paramsbst[i], paramsmax, w)

            objmax[j] = paramsmax.objval
            print 'Swarm iteration:', j+1, ', Best objfun value:', objmax[j]

            if j > 0:
                # Count no. of swarm iterations with no objective function value improvement
                abser = objmax[j] - objmax[j-1]
                if abser < ertol:
                    nstp += 1
                else:
                    nstp = 0

            # Stop the optimisation if maximum swarm iterations have been
            # reached without any improvement in the objective function value
            if nstp == maxiter:
                break

            w -= ((winit - wend)/(niter - 1))

        return paramsmax

    # ----------------------------------------------------------------

    @staticmethod
    def montecarlo_maximise(model, params, obsdata, objf, calperiods_obs, calperiods_sim):

        """ This method optimises a user provided model by maximising the user provided
        objective function with the MonteCarlo Optimisation algorithm.

        Args:
            (1) model: Instance of the user provided model.

            (2) params: List of the instances of user provided model parameter sets.

            (3) obsdata: Time-series of the observed data (that will be compared with simulated data).

            (4) objf: Method from the ObjectiveFunction class specifying the objective function.

            (5) calperiods_obs: Two element array (or list) specifying the index values of the start
                            and end data points of calibration period for the observed data.

            (6) calperiods_sim: Two element array (or list) specifying the index values of the start
                            and end data points of calibration period for the simulated data.

        """

        paramsmax = params[0]
        niter = len(params)  # No. of iterations

        # Start Monte-Carlo iterations
        for i in range(niter):

            # Simulate the model
            simdata = model.simulate(params[i])

            # Calculate the objective function value of simulation
            params[i].objval = objf(obsdata[calperiods_obs[0]:calperiods_obs[1]+1],
                                    simdata[calperiods_sim[0]:calperiods_sim[1]+1])

            # If current parameter set has improved upon previous maximum objective function value
            if params[i].objval > paramsmax.objval:
                # copy parameter set
                paramsmax = copy.deepcopy(params[i])

            print 'Iteration:', i+1, ', Best objfun value:', paramsmax.objval

        return paramsmax

######################################################################
