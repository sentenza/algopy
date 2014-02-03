##   Algopy - Python shell script that serves common algorhitms
##   Copyright (C) 2014 Alfredo Torre
##
##   This program is free software: you can redistribute it and/or modify
##   it under the terms of the GNU General Public License as published by
##   the Free Software Foundation, either version 3 of the License, or
##   (at your option) any later version.
##
##   This program is distributed in the hope that it will be useful,
##   but WITHOUT ANY WARRANTY; without even the implied warranty of
##   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
##   GNU General Public License for more details.
##
##   You should have received a copy of the GNU General Public License
##   along with this program. If not, see <http://www.gnu.org/licenses/>.

class Sort(object):
    """ Sorting algorithms """

    #def __init__(self):

    def bubbleSort(self, values, enhanced=False, verbose=False):
        """ Executing bubble sort algorithm on the list 'values'. 'values' is passed by reference! '"""
        if verbose:
            print "Executing bubble sort..."
        swaps = True
        for pas in range(1,len(values)):
            print "Passaggio %d" % pas
            if enhanced:
                maxpas = len(values) - pas 
                if swaps is not True:
                    return
                else:
                    swaps = False
            else:
                maxpas = len(values) - 1
            for n in range(0, maxpas):
                if(values[n] > values[n+1]):
                    values[n], values[n+1] = values[n+1], values[n] # swap
                    print "Scambio %d" % (n+1)
                    swaps = True
