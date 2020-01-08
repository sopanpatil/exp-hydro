# EXP-HYDRO Hydrological Model

EXP-HYDRO is a catchment scale hydrological model that operates at a daily time-step. It takes as inputs the daily values of precipitation, air temperature, and potential evapotranspiration, and simulates daily streamflow at the catchment outlet. This model was originally developed by Dr Sopan Patil in 2010 as part of his PhD research. Our research group (http://sopanpatil.weebly.com) continues its active development in both spatially lumped and spatially distributed configurations.  The name EXP-HYDRO is an acronym for Exponential Bucket Hydrological Model.

The source code provided is written in Python programming language and has been tested using Python 3.7.

The following data from a sample catchment are provided (in SampleData folder) to test the model code: P_test.txt (Precipitation data), T_test.txt (Air temperature data), PET_test.txt (Potential evapotranspiration data), Q_test.txt (catchment streamflow data).

- - - -

INSTALLATION:

Linux/Mac OS X:

After downloading and extracting the exp-hydro folder from GitHub, open Terminal and navigate to the exp-hydro folder which contains the `setup.py` file.  Make sure that you have administrator priveleges (can be obtained by typing `su` in Linux).  Then, type the following command:

```bash
python3 setup.py install
```

Windows:

Use command prompt to navigate to the downloaded exp-hydro folder, and type the following command:

```bash
setup.py install
```

This will install `exphydro` and all its dependent packages on your computer.

- - - -

SPATIALLY LUMPED VERSION:

Following execution files have been provided to quickly test the spatially lumped version of EXP-HYDRO (use these as an example to set up your own model run):

(1) `Run_exphydro_lumped_pso.py`: This calibrates EXP-HYDRO parameters using the Particle Swarm Optimisation (fast method).

(2) `Run_exphydro_lumped_mc.py`: This calibrates EXP-HYDRO parameters using a simple Monte Carlo method (slow method).

(3) `Run_exphydro_lumped_singlerun.py`: This performs a single model run of EXP-HYDRO, but the user has to specify the model parameters beforehand.

- - - -

SPATIALLY DISTRIBUTED VERSION:

Four types of spatially distributed EXP-HYDRO models have been included in the code.

Type 1: A Type 1 model is a pixel based distributed model where all pixels receive the same meteorological inputs.

Type 2: A Type 2 model is a pixel based distributed model where each pixel receives its own meteorological inputs.

Type 3: A Type 3 model is a sub-catchment based distributed model where all sub-catchments receive the same meteorological inputs.  The main difference compared to the pixel based model is that the sub-catchments can have different drainage areas, whereas all pixels have the same area.  An extra input argument 'subcatwts' is needed to initialise the ExpHydroDistrModel object for Type 3.  'subcatwts' is an array containing the areal weights of all sub-catchments and the sum of all array elements is 1.

Type 4: A Type 4 model is a sub-catchment based distributed model (like Type 3) where each sub-catchment receives its own meteorological inputs.

Only one execution file has been provided to quickly test the Type 1 distributed model (`Run_exphydro_distributed_type1_pso.py`).  This code calibrates the EXP-HYDRO parameters using the Particle Swarm Optimisation method for Type 1 model.

- - - -

SYSTEM REQUIREMENTS:

Please make sure that the following Python packages are installed on your computer before running any of the above execution files:
(1) NumPy (http://www.numpy.org/)
(2) SciPy (http://www.scipy.org/)
(3) matplotlib (http://matplotlib.org/)

- - - -

RELEVANT CITATION:

Patil, S. and M. Stieglitz (2014) Modelling daily streamflow at ungauged catchments: What information is necessary?, Hydrological Processes, 28(3), 1159-1169, doi:10.1002/hyp.9660.
