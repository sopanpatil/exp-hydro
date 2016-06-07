#!/usr/bin/env python

# Programmer(s): Sopan Patil.
# This file is part of the 'exphydro.utils' package.

import datetime
import numpy


######################################################################

class Daily2monthly(object):

    """ The 'Daily2monthly' class contains methods to convert daily data into monthly data.

    """

    @staticmethod
    def summation(dailydata, yyyy, mm, dd):

        """ This method converts daily data into monthly data by summing up all the data values
        in a given month.  It is suitable for data such as rainfall.

        Args:
            (1) dailydata: Time series of daily data

            (2) yyyy: Calendar year of the first day in dailydata

            (3) mm: Calendar month of the first day in dailydata

            (4) dd: Calendar day of the first day in dailydata

        """

        daystart = datetime.date(yyyy, mm, dd)  # This is the date of first day in daily time-series

        # Create a date array that is the same length as the daily data
        dayarr = numpy.array([daystart + datetime.timedelta(days=i) for i in xrange(dailydata.shape[0])])

        mondatatmp = dailydata[0]  # Store first day's value into a temporary variable
        mondata = []

        for j in range(1, dayarr.shape[0]):
            if dayarr[j].month == dayarr[j-1].month:  # If j is in the same month
                mondatatmp += dailydata[j]
            else:
                mondata = numpy.append(mondata, mondatatmp)  # Writing monthly summation into mondata variable
                mondatatmp = dailydata[j]  # Reset mondatatmp variable on the first day of month

            if j == dayarr.shape[0] - 1:  # If j is on the last day of time-series
                mondata = numpy.append(mondata, mondatatmp)  # Add the data from last month

        return mondata

    # ----------------------------------------------------------------

    @staticmethod
    def average(dailydata, yyyy, mm, dd):

        """ This method converts daily data into monthly data by averaging all the data values
            in a given month.  It is suitable for data such as air temperature.

        Args:
            (1) dailydata: Time series of daily data

            (2) yyyy: Calendar year of the first day in dailydata

            (3) mm: Calendar month of the first day in dailydata

            (4) dd: Calendar day of the first day in dailydata

            """

        daystart = datetime.date(yyyy, mm, dd)  # This is the date of first day in daily time-series

        # Create a date array that is the same length as the daily data
        dayarr = numpy.array([daystart + datetime.timedelta(days=i) for i in xrange(dailydata.shape[0])])

        mondatatmp = dailydata[0]  # Store first day's value into a temporary variable
        k = 1.0
        mondata = []

        for j in range(1, dayarr.shape[0]):
            if dayarr[j].month == dayarr[j - 1].month:  # If j is in the same month
                mondatatmp += dailydata[j]
                k += 1.0  # increase the day count
            else:
                mondata = numpy.append(mondata, [mondatatmp/k])  # Writing monthly average into mondata variable
                mondatatmp = dailydata[j]  # Reset mondatatmp variable on the first day of month
                k = 1.0  # reset the k counter to 1 at the start of the month

            if j == dayarr.shape[0] - 1:  # If j is on the last day of time-series
                mondata = numpy.append(mondata, [mondatatmp/k])  # Add the data from last month

        return mondata

######################################################################
