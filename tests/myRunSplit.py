#!/usr/bin/env python
import os
import sys
from BjSimulation import *

bjsim.player_list[0].resetPlayer()
bjsim.setBet(0)

bjsim.player_list[0].hands[0] = [Card(0, 8), Card(1, 8)]
bjsim.curr_game.shoe.cards[0] = Card(1, 8)
bjsim.curr_game.shoe.cards[1] = Card(1, 14)
bjsim.curr_game.shoe.cards[2] = Card(1, 8)
bjsim.curr_game.shoe.cards[3] = Card(1, 3)
bjsim.curr_game.shoe.cards[4] = Card(1, 8)
bjsim.curr_game.shoe.cards[5] = Card(1, 8)
bjsim.curr_game.shoe.cards[6] = Card(1, 8)
bjsim.curr_game.shoe.cards[7] = Card(1, 8)
bjsim.curr_game.shoe.cards[8] = Card(1, 8)
bjsim.curr_game.shoe.cards[9] = Card(1, 8)
bjsim.curr_game.shoe.cards[10] = Card(1, 8)
bjsim.curr_game.shoe.cards[11] = Card(1, 8)
bjsim.curr_game.shoe.cards[12] = Card(1, 8)
bjsim.curr_game.shoe.cards[13] = Card(1, 8)

bjsim.playHand(0, 0)
bjsim.printCurrGameState()
