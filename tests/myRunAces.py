#!/usr/bin/env python
import os
import sys
from BjSimulation import *

bjsim.player_list[0].resetPlayer()
bjsim.setBet(0)

bjsim.player_list[0].hands[0] = [Card(0, 14), Card(1, 14)]
bjsim.currGame.shoe.cards[0] = Card(1, 14)
bjsim.currGame.shoe.cards[1] = Card(1, 7)
bjsim.currGame.shoe.cards[2] = Card(1, 14)
bjsim.currGame.shoe.cards[3] = Card(1, 3)
bjsim.currGame.shoe.cards[4] = Card(1, 8)
bjsim.currGame.shoe.cards[5] = Card(1, 8)
bjsim.currGame.shoe.cards[6] = Card(1, 8)

bjsim.playHand(0, 0)
bjsim.printCurrGameState()
bjsim.payoutWinners()
bjsim.printStandings()
