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

    # Modify config to work for this test
    config["rounds_to_play"] = 1
    config["min_bet"] = 1
    config["num_decks"] = 2
    config["starting_chips"] = [0, 0, 0]
    config["player_name_list"] = ["Basic", "Felt", "HiLo"]
    config["player_adjust_betting_list"] = ["Basic", "Felt", "HiLo"]
    config["num_players"] = 3

    bjsim = BjSimulation(config)
    bjsim.curr_game = GameState(bjsim.num_decks, bjsim.penetration_min, bjsim.penetration_max)

    # Increase the TC to 2 for advantage players
    ############################################

    # Rank 2 increases count by 1 for HiLo and Felt
    for i in range(2*bjsim.num_decks):
        bjsim.curr_game.shoe.cards[0] = Card(1, 2)
        bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == 2*bjsim.num_decks)
    assert(bjsim.curr_game.felt_true_count == 2)
    assert(bjsim.curr_game.hilo_run_count  == 2*bjsim.num_decks)
    assert(bjsim.curr_game.hilo_true_count == 2)
    
    #
    # TEST CASE
    #  Give all players blackjack and ensure no bankroll changes after 
    ############################################################################
    
    bjsim.curr_game.shoe.cards[0] = Card(1, 14)
    bjsim.curr_game.shoe.cards[1] = Card(1, 14)
    bjsim.curr_game.shoe.cards[2] = Card(1, 14)
    bjsim.curr_game.shoe.cards[3] = Card(1, 14)
    bjsim.curr_game.shoe.cards[4] = Card(1, 11)
    bjsim.curr_game.shoe.cards[5] = Card(1, 11)
    bjsim.curr_game.shoe.cards[6] = Card(1, 11)
    bjsim.curr_game.shoe.cards[7] = Card(1, 11)

    bjsim.simulateHand()

    assert(bjsim.player_list[0].bet == 1)
    assert(bjsim.player_list[1].bet == 3)
    assert(bjsim.player_list[2].bet == 3)
    assert(bjsim.player_list[0].chips == 0)
    assert(bjsim.player_list[1].chips == 0)
    assert(bjsim.player_list[2].chips == 0)
    
    print "SUCCESS!"
