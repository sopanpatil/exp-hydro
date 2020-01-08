from setuptools import setup

setup(name='exphydro',
      version='1.2',
      description='EXP-HYDRO hydrological model',
      author='Sopan Patil and Marc Stieglitz',
      license='MIT',
      packages=['exphydro'],
      install_requires=['numpy', 'scipy', 'matplotlib', 'hydroutils'],
      dependency_links=['https://github.com/sopanpatil/hydroutils/tarball/master#egg=hydroutils-1.1'],
      classifiers=[
          'Programming Language :: Python :: 3.7',
          'License :: OSI Approved :: MIT License',
          'Topic :: Scientific/Engineering',
          'Intended Audience :: Science/Research'
      ],
      )
