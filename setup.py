from setuptools import setup

setup(name='exphydro',
	version='1.0',
	description='EXP-HYDRO hydrological model',
	author='Sopan Patil and Marc Stieglitz',
	license='MIT',
	packages=['exphydro'],
	install_requires=['numpy','scipy','matplotlib'],
	classifiers=[
		'Programming Language :: Python :: 2.7',
		'License :: OSI Approved :: MIT License',
		'Topic :: Scientific/Engineering',
		],
	)

