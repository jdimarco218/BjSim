#!/usr/bin/env python
import os
import sys
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)))

from BjSimulation import *

sys.argv = ['RunBjSimulation.py', 'config.py']

# INPUT TEST CASES HERE
#######################
def runAllTests():
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
    # Player 20, dealer blackjack
    p_hand_list = [Card(1, 10), Card(2, 11)]
    d_hand_list = [Card(2, 12), Card(3, 14)]
    testHand(p_hand_list, d_hand_list, [], 2, -2, 0, 0)
    # Player 4, dealer blackjack
    p_hand_list = [Card(1, 2), Card(2, 2)]
    d_hand_list = [Card(2, 12), Card(3, 14)]
    testHand(p_hand_list, d_hand_list, [], 2, -2, 0, 0)
    return


def testHand(p_hand_list, d_hand_list, top_of_shoe_list, bet, expected_payout, expected_splits, expected_doubles_count):

    # SETUP
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
