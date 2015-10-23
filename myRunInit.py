#!/usr/bin/env python
import os
import sys
from BjSimulation import *

sys.argv = ['RunBjSimulation.py', 'config.py']

if len(sys.argv) != 2:
    print "Usage:"
    print "  RunBjSimulation.py <inputConfigurationFile>"
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
