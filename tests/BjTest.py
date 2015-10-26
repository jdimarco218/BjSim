#!/usr/bin/env python
import os
import sys
import __main__ as main

if hasattr(main, '__file__'):
    sys.path.append(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)))

from BjSimulation import *

sys.argv = ['RunBjSimulation.py', 'config.py']
#
# INPUT TEST CASES HERE
#######################
def runAllTests():
    #
    # Blackjack hands
    #---------------------------------------------------------------------------
    # Player blackjack, dealer blackjack no ace up
    p_hand_list = [Card(1, 14), Card(2, 11)]
    d_hand_list = [Card(2, 12), Card(3, 14)]
    testHand(p_hand_list, d_hand_list, [], 2, 0, 0, 0)
    # Player blackjack, dealer blackjack ace up
    p_hand_list = [Card(1, 14), Card(2, 11)]
    d_hand_list = [Card(2, 14), Card(3, 12)]
    testHand(p_hand_list, d_hand_list, [], 2, 0, 0, 0)
    # Player blackjack, dealer no blackjack
    p_hand_list = [Card(1, 14), Card(2, 11)]
    d_hand_list = [Card(2, 12), Card(3, 12)]
    testHand(p_hand_list, d_hand_list, [], 2, 3, 0, 0)
    # Player 20, dealer blackjack no ace up
    p_hand_list = [Card(1, 10), Card(2, 11)]
    d_hand_list = [Card(2, 12), Card(3, 14)]
    testHand(p_hand_list, d_hand_list, [], 2, -2, 0, 0)
    # Player 20, dealer blackjack with ace up
    p_hand_list = [Card(1, 10), Card(2, 11)]
    d_hand_list = [Card(2, 14), Card(3, 11)]
    testHand(p_hand_list, d_hand_list, [], 2, -2, 0, 0)
    # Player 4 and shouldn't play, dealer blackjack no ace up
    p_hand_list = [Card(1, 2), Card(2, 2)]
    d_hand_list = [Card(2, 12), Card(3, 14)]
    testHand(p_hand_list, d_hand_list, [], 2, -2, 0, 0)
    # Player 4 and shouldn't play, dealer blackjack with ace up
    p_hand_list = [Card(1, 2), Card(2, 2)]
    d_hand_list = [Card(2, 14), Card(3, 13)]
    testHand(p_hand_list, d_hand_list, [], 2, -2, 0, 0)
    #
    # Splitting 2's
    #---------------------------------------------------------------------------
    # Player gets pair of 2s and splits against a 7, doubles both one wins pushes other, dealer 18
    p_hand_list = [Card(1, 2), Card(2, 2)]
    d_hand_list = [Card(2, 7), Card(3, 14)]
    testHand(p_hand_list, d_hand_list, [Card(3, 8), Card(3, 8), Card(0, 8), Card(1, 9)], 2, 4, 1, 2)
    # Player gets pair of 2s and  doesnt split against an 8, dealer 18
    p_hand_list = [Card(1, 2), Card(2, 2)]
    d_hand_list = [Card(2, 8), Card(3, 13)]
    testHand(p_hand_list, d_hand_list, [Card(3, 8), Card(3, 5)], 2, -2, 0, 0)
    #
    # Splitting 3's
    #---------------------------------------------------------------------------
    # Player gets pair of 3s and splits against a 7, doubles both one wins pushes other, dealer 18
    p_hand_list = [Card(1, 3), Card(2, 3)]
    d_hand_list = [Card(2, 7), Card(3, 14)]
    testHand(p_hand_list, d_hand_list, [Card(3, 7), Card(3, 8), Card(0, 7), Card(1, 9)], 2, 4, 1, 2)
    # Player gets pair of 3s and  doesnt split against an 8, dealer 18
    p_hand_list = [Card(1, 3), Card(2, 3)]
    d_hand_list = [Card(2, 8), Card(3, 13)]
    testHand(p_hand_list, d_hand_list, [Card(3, 6), Card(3, 5)], 2, -2, 0, 0)
    #
    # Splitting 4's
    #---------------------------------------------------------------------------
    # Player gets pair of 4s and doesnt splits against a 4, cannot double and wins
    p_hand_list = [Card(1, 4), Card(2, 4)]
    d_hand_list = [Card(2, 4), Card(3, 6)]
    testHand(p_hand_list, d_hand_list, [Card(3, 2), Card(3, 8), Card(0, 7)], 2, 2, 0, 0)
    # Player gets pair of 4s and splits against a 5, doubles one wins, standard wins other, dealer breaks
    p_hand_list = [Card(1, 4), Card(2, 4)]
    d_hand_list = [Card(2, 5), Card(3, 5)]
    testHand(p_hand_list, d_hand_list, [Card(3, 5), Card(3, 14), Card(0, 2), Card(0, 5), Card(1, 2), Card(3, 5), Card(2, 7)], 2, 6, 1, 1)
    # Player gets pair of 4s and doesnt splits against a 7, cannot double and loses
    p_hand_list = [Card(1, 4), Card(2, 4)]
    d_hand_list = [Card(2, 7), Card(3, 14)]
    testHand(p_hand_list, d_hand_list, [Card(3, 2), Card(3, 7)], 2, -2, 0, 0)
    #
    # Not Splitting 5's
    #---------------------------------------------------------------------------
    # Player gets pair of 5s and doesnt split against an 8, doubles and wins 
    p_hand_list = [Card(1, 5), Card(2, 5)]
    d_hand_list = [Card(2, 8), Card(3, 9)]
    testHand(p_hand_list, d_hand_list, [Card(3, 9)], 2, 4, 0, 1)
    # Player gets pair of 5s and doesnt split against an A, hits and loses 
    p_hand_list = [Card(1, 5), Card(2, 5)]
    d_hand_list = [Card(2, 14), Card(3, 9)]
    testHand(p_hand_list, d_hand_list, [Card(3, 9)], 2, -2, 0, 0)
    #
    # Max Split Tests (uses 4 total hands at time of writing)
    #---------------------------------------------------------------------------
    # Player splits 4 7s, gets three doubles and can't split the fourth and hits, dealer 10 showing and makes 18 
    p_hand_list = [Card(1, 7), Card(2, 7)]
    d_hand_list = [Card(2, 7), Card(3, 14)]
    testHand(p_hand_list, d_hand_list, [Card(3, 7), Card(3, 4), Card(2, 13), Card(2, 4), Card(2, 12), Card(1, 7), Card(2, 4), Card(1, 10), Card(3, 7), Card(3, 8)], 2, 10, 3, 3)
    # Player splits 4 7s, doubles one for a push, doubles one for a win, loses the other two, dealer 10 showing and makes 18 
    p_hand_list = [Card(1, 7), Card(2, 7)]
    d_hand_list = [Card(2, 7), Card(3, 14)]
    testHand(p_hand_list, d_hand_list, [Card(3, 7), Card(3, 4), Card(2, 7), Card(2, 4), Card(2, 10), Card(1, 7), Card(2, 5), Card(1, 10), Card(3, 7), Card(3, 3)], 2, 0, 3, 2)
    #
    # Misc Tests
    #---------------------------------------------------------------------------
    # Player gets 11 on three cards and shouldnt double, dealer 18
    p_hand_list = [Card(1, 2), Card(2, 3)]
    d_hand_list = [Card(2, 7), Card(3, 14)]
    testHand(p_hand_list, d_hand_list, [Card(3, 6), Card(3, 9)], 2, 2, 0, 0)
    # Player doubles and should lose and not draw the winning card (a three), dealer 18
    p_hand_list = [Card(1, 7), Card(2, 4)]
    d_hand_list = [Card(2, 7), Card(3, 14)]
    testHand(p_hand_list, d_hand_list, [Card(3, 6), Card(3, 3)], 2, -4, 0, 1)
    return


def testHand(p_hand_list, d_hand_list, top_of_shoe_list, bet, expected_payout, expected_splits, expected_doubles_count):

    # SETUP
    bjsim.player_list[0].resetPlayer()
    bjsim.player_list[0].chips = 0-bet
    bjsim.player_list[0].bet = bet 
    bjsim.player_list[0].active = True
    # END SETUP

    bjsim.player_list[0].hands[0] = p_hand_list 
    bjsim.dealer.hands[0]         = d_hand_list
    
    for i in range(len(top_of_shoe_list)):
        # Overwrite the shoe cards with what we want
        bjsim.curr_game.shoe.cards[i] = top_of_shoe_list[i]

    # Run BjSimulation
    bjsim.checkForInsuranceAndBlackjack()
    if bjsim.player_list[0].active:
        bjsim.playHand(0)
    bjsim.playDealer()
    bjsim.payoutWinners()
        
    # Check results
    assert(expected_payout == bjsim.player_list[0].chips)
    assert(expected_splits == (len(bjsim.player_list[0].hands)-1))
    num_doubles = 0
    for i in range(len(bjsim.player_list[0].double_list)):
        if bjsim.player_list[0].double_list[i]:
            num_doubles += 1
    assert(expected_doubles_count == num_doubles)


#
# Entry Point
#-------------------------------------------------------------------------------
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
    config["num_decks"] = 6
    config["starting_chips"] = [0]
    config["player_name_list"] = ["Basic"]
    config["player_adjust_betting_list"] = ["Basic"]
    config["num_players"] = 1

    bjsim = BjSimulation(config)
    bjsim.curr_game = GameState(bjsim.num_decks, bjsim.penetration_min, bjsim.penetration_max)

    runAllTests()
    print "SUCCESS!"

