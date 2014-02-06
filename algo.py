#!/usr/bin/env python

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
import sys
try:
    import argparse
except ImportError, e:
    sys.stderr.write('ERROR: %s\n' % str(e))
    sys.stderr.write("You must install argparse: https://pypi.python.org/pypi/argparse")
    sys.exit(1)
import subprocess
import logging
from algorithms.sort import Sort

if sys.version_info < (2, 6):
    print('ERROR: %s' % sys.exc_info()[1])
    print('ERROR: this script requires Python 2.6 or greater.')
    sys.exit(101)

# Create variables out of shell commands
# Note triple quotes can embed Bash

# You could add another bash command here
# HOLDING_SPOT="""fake_command"""
    
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def runBash(cmd):
    """ Takes Bash commands and returns them  """
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out = p.stdout.read().strip()
    return out  #This is the stdout from the shell command

# TODO: suppress VERBOSE
VERBOSE=False
def report(output,cmdtype="UNIX COMMAND:"):
    """ if VERBOSE==true prints the command type and the output of the command """
    #Notice the global statement allows input from outside of function
    if VERBOSE:
        print "%s: %s" % (cmdtype, output)
    else:
        print output


#Function to control option parsing in Python
def controller():
    """ Controls the argument parsing with argparse module """
    global VERBOSE
    logger.info("controller method")
    sorter = Sort()

    # Create instance of argparse.ArgumentParser Module, included in Standard Library from Python>=2.7
    parser = argparse.ArgumentParser(prog="algopy", description="Python shell script that serves common algorithms");
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('-v', '--verbose', default=False)
    parser.add_argument('-a', '--array', nargs='+', type=int, help="A list of numbers", dest="values")
    parser.add_argument('-s', '--sort', help="Sorting algorithm", nargs='?', const="bubble", choices=['bubble'], 
            metavar=('bubble'))

    #Option Handling passes correct parameter to runBash
    arguments = parser.parse_args()
    if arguments.verbose:
        VERBOSE=True
    if arguments.values is not None and arguments.sort is not None:
        sorter.bubbleSort(arguments.values, enhanced=True)
        print "Values ordered: %s" % arguments.values
    else:
        parser.print_help()

def main():
    # Other checks and operations could be embed here - before the arguments parsing
    controller()

if __name__ == '__main__':
    main()
