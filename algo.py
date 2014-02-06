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

__version__ = "0.1"

if sys.version_info < (2, 6):
    print('ERROR: %s' % sys.exc_info()[1])
    print('ERROR: this script requires Python 2.6 or greater.')
    sys.exit(101)

# Create variables out of shell commands
# Note triple quotes can embed Bash

# You could add another bash command here
# HOLDING_SPOT="""fake_command"""
    


def runBash(cmd):
    """ Takes Bash commands and returns them  """
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out = p.stdout.read().strip()
    return out  #This is the stdout from the shell command

def report(output,cmdtype="UNIX COMMAND:"):
    #Notice the global statement allows input from outside of function
    logger.info("%s: %s" % (cmdtype, output))

def _logging_level(level):
    LEVELS = [logging.DEBUG, logging.INFO, logging.WARN, logging.ERROR, logging.FATAL]
    if level is None:
        logging.basicConfig(level=LEVELS[-1]) # CRITICAL level is the default one
    elif level > len(LEVELS)-1 :
        logging.basicConfig(level=LEVELS[0]) # Too much -v -> go to debug
    else:
        logging.basicConfig(level=LEVELS[-level-1])


#Function to control option parsing in Python
def controller():
    """ Controls the argument parsing with argparse module """
    global logger
    sorter = Sort()

    # Create instance of argparse.ArgumentParser Module, included in Standard Library from Python>=2.7
    parser = argparse.ArgumentParser(prog="algopy", description="Python shell script that serves common algorithms");
    parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=__version__), 
            help='show the program version')
    parser.add_argument('-v', '--verbose', action='count', help='Increase verbosity')
    parser.add_argument('-a', '--array', nargs='+', type=int, help="A list of numbers", dest="values")
    parser.add_argument('-s', '--sort', help="Sorting algorithm", nargs='?', const="bubble", choices=['bubble'], 
            metavar=('bubble'))

    #Option Handling passes correct parameter to runBash
    arguments = parser.parse_args()
    _logging_level(arguments.verbose)
    logger = logging.getLogger(__name__)
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
