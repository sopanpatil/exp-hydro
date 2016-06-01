#!/usr/bin/env python

# Programmer(s): Sopan Patil.
# This file is part of the 'exphydro.utils' package.

import numpy


######################################################################

class ObjectiveFunction(object):

    """ The 'ObjectiveFunction' class contains the following two commonly used objective functions:
    (1) Kling-Gupta efficiency

    (2) Nash-Sutcliffe efficiency

    """

    @staticmethod
    def klinggupta(obsdata, simdata):

        """ This method calculates Kling-Gupta efficiency
        of the simulated data timeseries.

        Args:
            (1) obsdata: Time series of the observed data.

            (2) simdata: Time series of the simulated data.

        """
        
        xbar = numpy.mean(obsdata)
        ybar = numpy.mean(simdata)
        nobs = obsdata.shape[0]
        numer = 0.0
        denom1 = 0.0
        denom2 = 0.0
    
        for i in range(nobs):
            numer += ((obsdata[i]-xbar)*(simdata[i]-ybar))
            denom1 += numpy.square(obsdata[i]-xbar)
            denom2 += numpy.square(simdata[i]-ybar)

        if denom2 == 0:
            kge = -9999
            return kge
        
        r = numer/(numpy.sqrt(denom1)*numpy.sqrt(denom2))
        alpha = numpy.sqrt(denom2/nobs)/numpy.sqrt(denom1/nobs)
        beta = ybar/xbar
        kge = 1.0 - numpy.sqrt(numpy.square(r-1.0) + numpy.square(alpha-1.0) + numpy.square(beta-1.0))
        return kge

    # ----------------------------------------------------------------

    @staticmethod
    def nashsutcliffe(obsdata, simdata):

        """ This method calculates Nash-Sutcliffe efficiency
        of the simulated data timeseries.

        Args:
            (1) obsdata: Time series of the observed data.

            (2) simdata: Time series of the simulated data.

        """
        
        xbar = numpy.mean(obsdata)
        nobs = obsdata.shape[0]
        numer = 0.0
        denom = 0.0

        for i in range(nobs):
            numer += numpy.square(obsdata[i] - simdata[i])
            denom += numpy.square(obsdata[i] - xbar)

        nse = 1.0 - (numer/denom)
        return nse

######################################################################
