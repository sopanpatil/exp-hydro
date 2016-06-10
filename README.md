# EXP-HYDRO Hydrological Model

EXP-HYDRO is a catchment scale hydrological model that operates at a daily time-step. It takes as inputs the daily values of precipitation, air temperature, and potential evapotranspiration, and simulates daily streamflow at the catchment outlet. This model was originally developed by Dr Sopan Patil in 2010 as part of his PhD research. Our research group (http://sopanpatil.weebly.com) continues its active development in both spatially lumped and spatially distributed configurations.  The name EXP-HYDRO is an acronym for Exponential Bucket Hydrological Model.

The source code provided is written in Python programming language and has been tested using Python 2.7.

The following data from a sample catchment are provided (in SampleData folder) to test the model code: P_test.txt (Precipitation data), T_test.txt (Air temperature data), PET_test.txt (Potential evapotranspiration data), Q_test.txt (catchment streamflow data).

SPATIALLY LUMPED VERSION:

Following are the execution files for running the spatially lumped version of EXP-HYDRO:
(1) Run_exphydro_lumped_pso.py: This calibrates EXP-HYDRO parameters using the Particle Swarm Optimisation (fast method).

(2) Run_exphydro_lumped_mc.py: This calibrates EXP-HYDRO parameters using a simple Monte Carlo method (slow method).

(3) Run_exphydro_lumped_singlerun.py: This performs a single model run of EXP-HYDRO, but the user has to specify the model parameters beforehand.

SPATIALLY DISTRIBUTED VERSION:

Four types of spatially distributed EXP-HYDRO models have been included in the code.

Type 1:

Type 2:

Type 3:

Type 4:

SYSTEM REQUIREMENTS:

Please make sure that the following Python packages are installed on your computer before running any of the above execution files:
(1) NumPy (http://www.numpy.org/)
(2) SciPy (http://www.scipy.org/)
(3) matplotlib (http://matplotlib.org/)

RELEVANT CITATION:

Patil, S. and M. Stieglitz (2014) Modelling daily streamflow at ungauged catchments: What information is necessary?, Hydrological Processes, 28(3), 1159-1169, doi:10.1002/hyp.9660.
