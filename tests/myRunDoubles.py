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
    config["rounds_to_play"] = 1
    bjsim = BjSimulation(config)

    # Go!
    bjsim.runSimulation()
    bjsim.curr_game.shoe.cards[0] = Card(1, 2)
    bjsim.curr_game.shoe.cards[1] = Card(1, 2)
    bjsim.curr_game.shoe.cards[2] = Card(1, 2)
    bjsim.curr_game.shoe.cards[3] = Card(1, 2)
    bjsim.curr_game.shoe.cards[4] = Card(1, 2)
    bjsim.curr_game.shoe.cards[5] = Card(1, 2)
    bjsim.curr_game.shoe.cards[6] = Card(1, 2)
    bjsim.curr_game.shoe.cards[7] = Card(1, 2)
    bjsim.curr_game.shoe.cards[8] = Card(1, 2)
    bjsim.curr_game.shoe.cards[9] = Card(1, 2)
    bjsim.curr_game.shoe.cards[10] = Card(1, 2)
    bjsim.curr_game.shoe.cards[11] = Card(1, 2)
    bjsim.curr_game.shoe.cards[12] = Card(1, 2)
    bjsim.curr_game.shoe.cards[13] = Card(1, 2)
    bjsim.curr_game.shoe.cards[14] = Card(1, 2)
    bjsim.curr_game.shoe.cards[15] = Card(1, 2)
    bjsim.curr_game.shoe.cards[16] = Card(1, 2)
    bjsim.curr_game.shoe.cards[17] = Card(1, 2)
    bjsim.curr_game.shoe.cards[18] = Card(1, 2)
    bjsim.curr_game.shoe.cards[19] = Card(1, 2)
    bjsim.curr_game.shoe.cards[20] = Card(1, 2)
    bjsim.curr_game.shoe.cards[21] = Card(1, 2)
    bjsim.curr_game.shoe.cards[22] = Card(1, 2)
    bjsim.curr_game.shoe.cards[23] = Card(1, 2)
    bjsim.curr_game.shoe.cards[24] = Card(1, 2)
    bjsim.curr_game.shoe.cards[25] = Card(1, 2)
    for i in range(25):
        bjsim.curr_game.shoe.popCard()
    print("Starting sim with counts:")
    print(" Felt- " + str(bjsim.curr_game.felt_true_count) + "(" + str(bjsim.curr_game.felt_run_count) + ")")
    print(" Hilo- " + str(bjsim.curr_game.hilo_true_count) + "(" + str(bjsim.curr_game.hilo_run_count) + ")")
    print("Prepping for three players to all double on splits and win...")
    bjsim.curr_game.shoe.cards[0] = Card(1, 7)
    bjsim.curr_game.shoe.cards[1] = Card(1, 7)
    bjsim.curr_game.shoe.cards[2] = Card(1, 7)
    bjsim.curr_game.shoe.cards[3] = Card(1, 6)
    bjsim.curr_game.shoe.cards[4] = Card(1, 7)
    bjsim.curr_game.shoe.cards[5] = Card(1, 7)
    bjsim.curr_game.shoe.cards[6] = Card(1, 7)
    bjsim.curr_game.shoe.cards[7] = Card(1, 10)
    bjsim.curr_game.shoe.cards[8] = Card(1, 7)
    bjsim.curr_game.shoe.cards[9] = Card(1, 4)
    bjsim.curr_game.shoe.cards[10] = Card(1, 10)
    bjsim.curr_game.shoe.cards[11] = Card(1, 4)
    bjsim.curr_game.shoe.cards[12] = Card(1, 10)
    bjsim.curr_game.shoe.cards[13] = Card(1, 4)
    bjsim.curr_game.shoe.cards[14] = Card(1, 10)
    bjsim.curr_game.shoe.cards[15] = Card(1, 7)
    bjsim.curr_game.shoe.cards[16] = Card(1, 4)
    bjsim.curr_game.shoe.cards[17] = Card(1, 10)
    bjsim.curr_game.shoe.cards[18] = Card(1, 4)
    bjsim.curr_game.shoe.cards[19] = Card(1, 10)
    bjsim.curr_game.shoe.cards[20] = Card(1, 4)
    bjsim.curr_game.shoe.cards[21] = Card(1, 10)
    bjsim.curr_game.shoe.cards[22] = Card(1, 7)
    bjsim.curr_game.shoe.cards[23] = Card(1, 4)
    bjsim.curr_game.shoe.cards[24] = Card(1, 10)
    bjsim.curr_game.shoe.cards[25] = Card(1, 4)
    bjsim.curr_game.shoe.cards[26] = Card(1, 10)
    bjsim.curr_game.shoe.cards[27] = Card(1, 4)
    bjsim.curr_game.shoe.cards[28] = Card(1, 10)
    bjsim.curr_game.shoe.cards[29] = Card(1, 10)
    bjsim.simulateHand()
    
    print "Done."
