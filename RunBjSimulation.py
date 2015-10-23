#!/usr/bin/env python
import sys
import os
from BjSimulation import *

###
#  The purpose of this script is to run/simulate a game of blackjack.  The run can be
#  played as a game, or run to gather empirical statistics about various rules/strategies.
#
#  Usage:
#    RunBjSimulation.py <inputConfiguration>
###

def main():
    if len(sys.argv) != 2:
        print "Usage:"
        print "  RunBjSimulation.py <inputConfigurationFile>"
        return
    else:
        # Get inputConfigurationFile and outputFile
        inputConfigFile = sys.argv[1]

        # Input configuration must be python syntax to set values
        config = {}
        execfile(inputConfigFile, config)
        bjsim = BjSimulation(config)

        # Go!
        bjsim.runSimulation()
        
        print "Done."
        return


# Entry point
if __name__ == "__main__":
    main()
