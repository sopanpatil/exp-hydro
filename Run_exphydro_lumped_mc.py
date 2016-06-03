#!/usr/bin/env python

# Programmer(s): Sopan Patil.

""" MAIN PROGRAM FILE
Run this file to optimise the EXP-HYDRO model parameters
using Monte Carlo optimisation algorithm.

Please note that this is a slow optimisation method compared to
Particle Swarm Optimisation (PSO), and requires a very large number
of iterations (> 10000) to get reliable optimisation.
"""

import numpy
import os
import matplotlib.pyplot as plt
from exphydro.lumped import ExphydroModel, ExphydroParameters
from exphydro.utils import Calibration, ObjectiveFunction

######################################################################
# SET WORKING DIRECTORY

# Getting current directory, i.e., directory containing this file
dir1 = os.path.dirname(os.path.abspath('__file__'))

# Setting to current directory
os.chdir(dir1)

######################################################################
# MAIN PROGRAM

# Load meteorological and observed flow data
P = numpy.genfromtxt('SampleData/P_test.txt')  # Observed rainfall (mm/day)
T = numpy.genfromtxt('SampleData/T_test.txt')  # Observed air temperature (deg C)
PET = numpy.genfromtxt('SampleData/PET_test.txt')  # Potential evapotranspiration (mm/day)
Qobs = numpy.genfromtxt('SampleData/Q_test.txt')  # Observed streamflow (mm/day)

# Specify the no. of iterations
niter = 100

# Generate 'niter' initial EXP-HYDRO model parameters
params = [ExphydroParameters() for j in range(niter)]

# Initialise the model by loading its climate inputs
model = ExphydroModel(P, PET, T)

# Specify the start and end day numbers of the calibration period.
# This is done separately for the observed and simulated data
# because they might not be of the same length in some cases.
calperiods_obs = [365, 2557]
calperiods_sim = [365, 2557]

# Calibrate the model to identify optimal parameter set
paramsmax = Calibration.montecarlo_maximise(model, params, Qobs, ObjectiveFunction.klinggupta, calperiods_obs, calperiods_sim)
print 'Calibration run KGE value = ', paramsmax.objval

# Run the optimised model for validation period
Qsim = model.simulate(paramsmax)
kge = ObjectiveFunction.klinggupta(Qobs[calperiods_obs[1]:], Qsim[calperiods_sim[1]:])
print 'Independent run KGE value = ', kge

# Plot the observed and simulated hydrographs
plt.plot(Qobs[calperiods_obs[0]:],'b-')
plt.hold(True)
plt.plot(Qsim[calperiods_sim[0]:],'r-')
plt.show()

######################################################################
