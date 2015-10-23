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
    config["player_name_list"] = ["Felt", "HiLo", "Basic"]
    config["player_adjust_betting_list"] = ["Felt", "HiLo", "Basic"]

    bjsim = BjSimulation(config)
    bjsim.curr_game = GameState(bjsim.num_decks, bjsim.penetration_min, bjsim.penetration_max)

    # Test different counts
    #######################

    # Simple count, 2
    bjsim.curr_game.shoe.cards[0] = Card(1, 2)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == 1)
    assert(bjsim.curr_game.felt_true_count == 0)
    assert(bjsim.curr_game.hilo_run_count  == 1)
    assert(bjsim.curr_game.hilo_true_count == 0)
    # Simple count, 3
    bjsim.curr_game.shoe.cards[0] = Card(1, 3)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == 3)
    assert(bjsim.curr_game.felt_true_count == 1)
    assert(bjsim.curr_game.hilo_run_count  == 2)
    assert(bjsim.curr_game.hilo_true_count == 1)
    # Simple count, 4
    bjsim.curr_game.shoe.cards[0] = Card(1, 4)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == 5)
    assert(bjsim.curr_game.felt_true_count == 2)
    assert(bjsim.curr_game.hilo_run_count  == 3)
    assert(bjsim.curr_game.hilo_true_count == 1)
    # Simple count, 5
    bjsim.curr_game.shoe.cards[0] = Card(1, 5)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == 7)
    assert(bjsim.curr_game.felt_true_count == 3)
    assert(bjsim.curr_game.hilo_run_count  == 4)
    assert(bjsim.curr_game.hilo_true_count == 2)
    # Simple count, 6
    bjsim.curr_game.shoe.cards[0] = Card(1, 6)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == 9)
    assert(bjsim.curr_game.felt_true_count == 4)
    assert(bjsim.curr_game.hilo_run_count  == 5)
    assert(bjsim.curr_game.hilo_true_count == 2)
    # Simple count, 7
    bjsim.curr_game.shoe.cards[0] = Card(1, 7)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == 10)
    assert(bjsim.curr_game.felt_true_count == 5)
    assert(bjsim.curr_game.hilo_run_count  == 5)
    assert(bjsim.curr_game.hilo_true_count == 2)
    # Simple count, 8
    bjsim.curr_game.shoe.cards[0] = Card(1, 8)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == 10)
    assert(bjsim.curr_game.felt_true_count == 5)
    assert(bjsim.curr_game.hilo_run_count  == 5)
    assert(bjsim.curr_game.hilo_true_count == 2)
    # Simple count, 9
    bjsim.curr_game.shoe.cards[0] = Card(1, 9)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == 10)
    assert(bjsim.curr_game.felt_true_count == 5)
    assert(bjsim.curr_game.hilo_run_count  == 5)
    assert(bjsim.curr_game.hilo_true_count == 2)
    # Simple count, 10
    bjsim.curr_game.shoe.cards[0] = Card(1, 10)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == 8)
    assert(bjsim.curr_game.felt_true_count == 4)
    assert(bjsim.curr_game.hilo_run_count  == 4)
    assert(bjsim.curr_game.hilo_true_count == 2)
    # Simple count, 11
    bjsim.curr_game.shoe.cards[0] = Card(1, 11)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == 6)
    assert(bjsim.curr_game.felt_true_count == 3)
    assert(bjsim.curr_game.hilo_run_count  == 3)
    assert(bjsim.curr_game.hilo_true_count == 1)
    # Simple count, 12
    bjsim.curr_game.shoe.cards[0] = Card(1, 12)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == 4)
    assert(bjsim.curr_game.felt_true_count == 2)
    assert(bjsim.curr_game.hilo_run_count  == 2)
    assert(bjsim.curr_game.hilo_true_count == 1)
    # Simple count, 13
    bjsim.curr_game.shoe.cards[0] = Card(1, 13)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == 2)
    assert(bjsim.curr_game.felt_true_count == 1)
    assert(bjsim.curr_game.hilo_run_count  == 1)
    assert(bjsim.curr_game.hilo_true_count == 0)
    # Simple count, 14
    bjsim.curr_game.shoe.cards[0] = Card(1, 14)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == 0)
    assert(bjsim.curr_game.felt_true_count == 0)
    assert(bjsim.curr_game.hilo_run_count  == 0)
    assert(bjsim.curr_game.hilo_true_count == 0)
    # Negative count, 14s
    bjsim.curr_game.shoe.cards[0] = Card(1, 14)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == -2)
    assert(bjsim.curr_game.felt_true_count == -1)
    assert(bjsim.curr_game.hilo_run_count  == -1)
    assert(bjsim.curr_game.hilo_true_count == -1)
    # Negative count, 14s
    bjsim.curr_game.shoe.cards[0] = Card(1, 14)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == -4)
    assert(bjsim.curr_game.felt_true_count == -2)
    assert(bjsim.curr_game.hilo_run_count  == -2)
    assert(bjsim.curr_game.hilo_true_count == -1)
    # Negative count, 14s
    bjsim.curr_game.shoe.cards[0] = Card(1, 14)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == -6)
    assert(bjsim.curr_game.felt_true_count == -3)
    assert(bjsim.curr_game.hilo_run_count  == -3)
    assert(bjsim.curr_game.hilo_true_count == -2)
    # Negative count, 14s
    bjsim.curr_game.shoe.cards[0] = Card(1, 14)
    bjsim.curr_game.shoe.popCard()
    assert(bjsim.curr_game.felt_run_count  == -8)
    assert(bjsim.curr_game.felt_true_count == -4)
    assert(bjsim.curr_game.hilo_run_count  == -4)
    assert(bjsim.curr_game.hilo_true_count == -2)
    
    print "SUCCESS!"
