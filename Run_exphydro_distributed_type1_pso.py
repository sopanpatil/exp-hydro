#!/usr/bin/env python

# Programmer(s): Sopan Patil.

""" MAIN PROGRAM FILE
Run this file to optimise the model parameters of the spatially distributed
version of EXP-HYDRO model using Particle Swarm Optimisation (PSO) algorithm.

Type 1 Model:
- This type of distributed model is pixel based (i.e., all sub-components
have the same drainage area).
- All pixels receive the same meteorological inputs.
- Channel routing is ignored and it is assumed that streamflow generated from
each pixel reaches the catchment outlet on same day.
"""

import numpy
import os
import time
import matplotlib.pyplot as plt
from exphydro.distributed import ExphydroDistrParameters
from exphydro.distributed.type1 import ExphydroDistrModel
from hydroutils import Calibration, ObjectiveFunction

start_time = time.time()

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

# Specify the number of pixels in the catchment
npixels = 5

# Specify the no. of parameter sets (particles) in a PSO swarm
npart = 10

# Generate 'npart' initial EXP-HYDRO model parameters
params = [ExphydroDistrParameters(npixels) for j in range(npart)]

# Initialise the model by loading its climate inputs
model = ExphydroDistrModel(P, PET, T, npixels)

# Specify the start and end day numbers of the calibration period.
# This is done separately for the observed and simulated data
# because they might not be of the same length in some cases.
calperiods_obs = [365, 2557]
calperiods_sim = [365, 2557]

# Calibrate the model to identify optimal parameter set
paramsmax = Calibration.pso_maximise(model, params, Qobs, ObjectiveFunction.klinggupta, calperiods_obs, calperiods_sim)
print ('Calibration run KGE value = ', paramsmax.objval)

# Run the optimised model for validation period
Qsim = model.simulate(paramsmax)
kge = ObjectiveFunction.klinggupta(Qobs[calperiods_obs[1]:], Qsim[calperiods_sim[1]:])
print ('Independent run KGE value = ', kge)

print("Total runtime: %s seconds" % (time.time() - start_time))

# Plot the observed and simulated hydrographs
plt.plot(Qobs[calperiods_obs[0]:], 'b-')
plt.plot(Qsim[calperiods_sim[0]:], 'r-')
plt.show()

######################################################################
