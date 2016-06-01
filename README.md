# EXP-HYDRO Hydrological Model

EXP-HYDRO is a catchment scale hydrological model that operates at a daily time-step. It takes as inputs the daily values of precipitation, air temperature, and potential evapotranspiration, and simulates daily streamflow at the catchment outlet. This model was originally developed by Dr Sopan Patil in 2010 as part of his PhD research. Our research group (http://sopanpatil.weebly.com) continues its active development in both spatially lumped and spatially distributed configurations.

The source code provided is written in Python programming language and has been tested using Python 2.7.

The following data from a sample catchment in Wales are provided (in SampleData folder) to test the model code: P_test.txt (Precipitation data), T_test.txt (Air temperature data), PET_test.txt (Potential evapotranspiration data), Q_test.txt (catchment streamflow data).

Following are the execution files for running EXP-HYDRO:
(1) Run_exphydro_lumped_pso.py: Performs a calibration and validation run of the lumped EXP-HYDRO model using Particle Swarm Optimisation (PSO) algorithm.
(2) Run_exphydro_distributed_pso.py: Performs a calibration and validation run of the distributed EXP-HYDRO model using PSO algorithm.

System Requirements: Please make sure that the following Python packages are installed on your computer before running any of the above execution files:
(1) NumPy (http://www.numpy.org/)
(2) SciPy (http://www.scipy.org/)
(3) matplotlib (http://matplotlib.org/)

Please cite as: Patil, S. and M. Stieglitz (2014) Modelling daily streamflow at ungauged catchments: What information is necessary?, Hydrological Processes, 28(3), 1159-1169, doi:10.1002/hyp.9660.
