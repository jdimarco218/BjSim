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
    #  Split and double by all players and push all hands against
    #  the dealer.  Ensure that no chips are gained/lost after
    ############################################################################
    
    bjsim.curr_game.shoe.cards[0] = Card(1, 7)
    bjsim.curr_game.shoe.cards[1] = Card(1, 7)
    bjsim.curr_game.shoe.cards[2] = Card(1, 7)
    bjsim.curr_game.shoe.cards[3] = Card(1, 7)
    bjsim.curr_game.shoe.cards[4] = Card(1, 7)
    bjsim.curr_game.shoe.cards[5] = Card(1, 7)
    bjsim.curr_game.shoe.cards[6] = Card(1, 7)
    bjsim.curr_game.shoe.cards[7] = Card(1, 4)
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

    assert(bjsim.player_list[0].bet == 1)
    assert(bjsim.player_list[1].bet == 3)
    assert(bjsim.player_list[2].bet == 3)
    assert(bjsim.player_list[0].chips == 0)
    assert(bjsim.player_list[1].chips == 0)
    assert(bjsim.player_list[2].chips == 0)

    # Ending count felt (7|14) hilo (2|4)

    #
    # TEST CASE
    #  Split to two hands
    #  Double first hand and lose
    #  Double first hand and lose
    #
    #  Ensure that they all lose the proper chips
    ############################################################################
    
    # Starting cards
    bjsim.curr_game.shoe.cards[0] = Card(1, 8)
    bjsim.curr_game.shoe.cards[1] = Card(1, 8)
    bjsim.curr_game.shoe.cards[2] = Card(1, 8)
    bjsim.curr_game.shoe.cards[3] = Card(1, 8)
    bjsim.curr_game.shoe.cards[4] = Card(1, 8)
    bjsim.curr_game.shoe.cards[5] = Card(1, 8)
    bjsim.curr_game.shoe.cards[6] = Card(1, 8)
    bjsim.curr_game.shoe.cards[7] = Card(1, 3)
    # Position 0
    bjsim.curr_game.shoe.cards[8] = Card(1, 3)
    bjsim.curr_game.shoe.cards[9] = Card(1, 2)
    bjsim.curr_game.shoe.cards[10] = Card(1, 3)
    bjsim.curr_game.shoe.cards[11] = Card(1, 2)
    # Position 1
    bjsim.curr_game.shoe.cards[12] = Card(1, 3)
    bjsim.curr_game.shoe.cards[13] = Card(1, 2)
    bjsim.curr_game.shoe.cards[14] = Card(1, 3)
    bjsim.curr_game.shoe.cards[15] = Card(1, 2)
    # Position 2
    bjsim.curr_game.shoe.cards[16] = Card(1, 3)
    bjsim.curr_game.shoe.cards[17] = Card(1, 2)
    bjsim.curr_game.shoe.cards[18] = Card(1, 3)
    bjsim.curr_game.shoe.cards[19] = Card(1, 2)
    # Dealer
    bjsim.curr_game.shoe.cards[20] = Card(1, 10)

    bjsim.simulateHand()

    assert(bjsim.player_list[0].bet == 1)
    assert(bjsim.player_list[1].bet == 8)
    assert(bjsim.player_list[2].bet == 3)
    assert(bjsim.player_list[0].chips == -1*4)
    assert(bjsim.player_list[1].chips == -8*4)
    assert(bjsim.player_list[2].chips == -3*4)

    # Ending count felt (32|32) hilo (16|16), bets cap at 8x currently

    #
    # TEST CASE
    #  Split to three hands by all players
    #  Double first and win
    #  Second hand win standard
    #  Third hand win standard
    #  
    #  Ensure that no chips are gained/lost after
    ############################################################################

    # Reset chips and counts to normalize
    bjsim.player_list[0].chips = 0
    bjsim.player_list[1].chips = 0
    bjsim.player_list[2].chips = 0
    bjsim.curr_game.felt_run_count = 4
    bjsim.curr_game.felt_true_count = 2
    bjsim.curr_game.hilo_run_count = 4
    bjsim.curr_game.hilo_true_count = 2
    
    # Starting cards
    bjsim.curr_game.shoe.cards[0] = Card(1, 8)
    bjsim.curr_game.shoe.cards[1] = Card(1, 8)
    bjsim.curr_game.shoe.cards[2] = Card(1, 8)
    bjsim.curr_game.shoe.cards[3] = Card(1, 8)
    bjsim.curr_game.shoe.cards[4] = Card(1, 8)
    bjsim.curr_game.shoe.cards[5] = Card(1, 8)
    bjsim.curr_game.shoe.cards[6] = Card(1, 8)
    bjsim.curr_game.shoe.cards[7] = Card(1, 3)
    # Position 0
    bjsim.curr_game.shoe.cards[8] = Card(1, 8)
    bjsim.curr_game.shoe.cards[9] = Card(1, 3)
    bjsim.curr_game.shoe.cards[10] = Card(1, 10)
    bjsim.curr_game.shoe.cards[11] = Card(1, 4)
    bjsim.curr_game.shoe.cards[12] = Card(1, 9)
    bjsim.curr_game.shoe.cards[13] = Card(1, 5)
    bjsim.curr_game.shoe.cards[14] = Card(1, 8)
    # Position 1
    bjsim.curr_game.shoe.cards[15] = Card(1, 8)
    bjsim.curr_game.shoe.cards[16] = Card(1, 3)
    bjsim.curr_game.shoe.cards[17] = Card(1, 10)
    bjsim.curr_game.shoe.cards[18] = Card(1, 4)
    bjsim.curr_game.shoe.cards[19] = Card(1, 9)
    bjsim.curr_game.shoe.cards[20] = Card(1, 5)
    bjsim.curr_game.shoe.cards[21] = Card(1, 8)
    # Position 2
    bjsim.curr_game.shoe.cards[22] = Card(1, 8)
    bjsim.curr_game.shoe.cards[23] = Card(1, 3)
    bjsim.curr_game.shoe.cards[24] = Card(1, 10)
    bjsim.curr_game.shoe.cards[25] = Card(1, 4)
    bjsim.curr_game.shoe.cards[26] = Card(1, 9)
    bjsim.curr_game.shoe.cards[27] = Card(1, 5)
    bjsim.curr_game.shoe.cards[28] = Card(1, 8)
    # Dealer
    bjsim.curr_game.shoe.cards[29] = Card(1, 2)
    bjsim.curr_game.shoe.cards[30] = Card(1, 10) 
    bjsim.simulateHand()

    assert(bjsim.player_list[0].bet == 1)
    assert(bjsim.player_list[1].bet == 3)
    assert(bjsim.player_list[2].bet == 3)
    assert(bjsim.player_list[0].chips == 1*4)
    assert(bjsim.player_list[1].chips == 3*4)
    assert(bjsim.player_list[2].chips == 3*4)

    #
    # TEST CASE
    #  Push on blackjacks
    #  
    #  Ensure that no chips are gained/lost after
    ############################################################################

    # Reset chips and counts to normalize
    bjsim.player_list[0].chips = 0
    bjsim.player_list[1].chips = 0
    bjsim.player_list[2].chips = 0
    bjsim.curr_game.felt_run_count = 4
    bjsim.curr_game.felt_true_count = 2
    bjsim.curr_game.hilo_run_count = 4
    bjsim.curr_game.hilo_true_count = 2
    
    # Starting cards
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
