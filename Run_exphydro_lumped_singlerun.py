#!/usr/bin/env python

# Programmer(s): Sopan Patil.

""" MAIN PROGRAM FILE
Run this file to perform a single run of the EXP-HYDRO model
with user provided parameter values.
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

# Initialise EXP-HYDRO model parameters object
params = ExphydroParameters()

# Specify the parameter values
# Please refer to Patil and Stieglitz (2014) for model parameter descriptions
params.f.value = 0.07       # f
params.smax.value = 200     # Smax
params.qmax.value = 20      # Qmax
params.ddf.value = 2        # Df
params.mint.value = -1      # Tmin
params.maxt.value = 1       # Tmax

# Initialise the model by loading its climate inputs
model = ExphydroModel(P, PET, T)

# Specify the start and end day numbers of the simulation period.
# This is done separately for the observed and simulated data
# because they might not be of the same length in some cases.
simperiods_obs = [365, 2557]
simperiods_sim = [365, 2557]

# Run the model and calculate objective function value for the simulation period
Qsim = model.simulate(params)
kge = ObjectiveFunction.klinggupta(Qobs[simperiods_obs[0]:simperiods_obs[1]+1], Qsim[simperiods_sim[0]:simperiods_sim[1]+1])
print 'KGE value = ', kge

# Plot the observed and simulated hydrographs
plt.plot(Qobs[simperiods_obs[0]:simperiods_obs[1]+1],'b-')
plt.hold(True)
plt.plot(Qsim[simperiods_sim[0]:simperiods_sim[1]+1],'r-')
plt.show()

######################################################################
