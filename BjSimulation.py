from __future__ import print_function

import os
import sys
import config
import random
from Card import Card
from Deck import Deck
from Shoe import Shoe


DEBUG = False
DEBUG_COUNT = False

class BjSimulation(object):
    """
    " Contains and runs a blackjack simulation for a given set of rules,
    " players, and strategy.
    "
    " Attributes:
    "   interactive_mode   - When set, allows the user to play the game. During
    "                        interactive mode, the count is hidden but can be
    "                        shown.  The play can be entered manually, or taken
    "                        from an input strategy. When unset, the games will
    "                        be run automatically while statistics are gathered
    "   num_decks          - The number of decks in the simulations Shoe
    "   stand_on_s17       - Whether or not the dealer plays on soft 17 
    "   surrender_allowed  - Whether or not the player is allowed to surrender
    "                        on the first two cards dealt
    "   double_after_split - Whether or not the player is allowed to double on
    "                        the first two cards after a split action
    "   num_splits         - The maximum number of splits. The maximum total
    "                        hands for the player is then num_splits+1
    "   penetration_min    - The minimum percentage of the Shoe that must be
    "                        played before a shuffle. The point at which a
    "                        shuffle is chosen is usually random between the
    "                        minimum and maximum range
    "   penetration_max    - The maximum percentage of the Shoe that must be
    "                        played before a shuffle.  The point at which a
    "                        shuffle is chosen is usually random between the
    "                        minimum and maximum range
    "   rounds_to_play     - Number of hands to play in the simulation. If this
    "                        is set to a negative number, then one of the other
    "                        termination conditions is used.
    "
    "   num_players        - Number of players to begin simulation with. This
    "                        can change dynamically if needed
    "   interactive_player_position 
    "                      - Where the user is seated at the table
    "   player_strategy_list 
    "                      - The list of input strategies to apply during
    "                        simulation
    " TODO
    """

    FACTOR_BLACKJACK = 2.5
    FACTOR_WIN       = 2.0
    FACTOR_DOUBLE    = 4.0
    FACTOR_PUSH      = 1.0
    FACTOR_SURRENDER = 0.5
    ACTION_STAND     = "S"
    ACTION_HIT       = "H"
    ACTION_SPLIT     = "P"
    ACTION_SURRENDER = "R"
    ACTION_DOUBLE    = "D"

    def __init__(self, config):
        # Refer to config.py for necessary values
        self.interactive_mode = config["interactive_mode"]
        self.num_decks = config["num_decks"]
        self.stand_on_s17 = config["stand_on_s17"]
        self.surrender_allowed = config["surrender_allowed"]
        self.double_after_split = config["double_after_split"]
        self.num_splits = config["num_splits"]
        self.penetration_min = config["penetration_min"]
        self.penetration_max = config["penetration_max"]
        self.rounds_to_play = config["rounds_to_play"]
        self.store_stats_after_shoe_count = config["store_stats_after_shoe_count"]
        self.min_bet = config["min_bet"]

        self.num_players = config["num_players"]
        self.interactive_player_position = config["interactive_player_position"]
        self.player_strategy_list = config["player_strategy_list"]
        self.player_adjust_betting_list = config["player_adjust_betting_list"]
        self.dealer_strategy = config["dealer_strategy"]
        self.player_starting_chips_list = config["player_starting_chips_list"]
        self.player_name_list = config["player_name_list"]
        self.player_list = []
        self.insurance_on_three_plus = config["insurance_on_three_plus"]
        self.player_indexing_list = config["player_strategy_list"]
        # Dealer holds the num_players'th position since they are zero indexed
        self.dealer = Player(self.num_players, self.dealer_strategy, 1000000, "Dealer")
        self.totalCount = 0
        self.curr_game = None
        for i in range(self.num_players):
            self.player_list.append(Player(i, self.player_strategy_list[i], self.player_starting_chips_list[i], self.player_name_list[i]))
        self.percent_done = 0

        # Save the current path to use when saving results
        self.dirPath = os.path.dirname(os.path.realpath(__file__))


    def simulationFinished(self):
        if self.rounds_to_play <= 0:
            return True
        else:
            self.rounds_to_play -= 1
            return False


    def runSimulation(self):
        self.curr_game = GameState(self.num_decks, self.penetration_min, self.penetration_max)
        for i in range(len(self.player_list)):
            self.player_list[i].shoes_played += 1
        burnCard = self.curr_game.shoe.popCard()
        if DEBUG:
            print("Shoe starting. Burning the top card: " + str(burnCard))
        while not self.simulationFinished():
            if len(self.curr_game.shoe.cards) < self.curr_game.cut_card:
                self.curr_game = GameState(self.num_decks, self.penetration_min, self.penetration_max)
                self.saveStatistics()
                for i in range(len(self.player_list)):
                    self.player_list[i].shoes_played += 1
                
            self.simulateHand()
            for i in range(len(self.player_list)):
                self.player_list[i].hands_played += 1
        self.finalizeStatistics()


    def saveStatistics(self):
        for i in range(len(self.player_list)):
            if not self.player_list[i].shoes_played % self.store_stats_after_shoe_count:
                if DEBUG:
                    print("Saving stats.")
                # Checkpoint this player's statistics
                relativePath = '/results/' + str(self.player_list[i].name) + '.csv'
                resultsPath = self.dirPath + relativePath
                if os.path.isfile(resultsPath):
                    sys.stdout = open(resultsPath, 'a')
                else:
                    sys.stdout = open(resultsPath, 'w')
                # Print comma separated values that we care about
                print(str(self.player_list[i].chips) + ",", end="")
                print(str(self.player_list[i].shoes_played) + ",", end="")
                print(str(self.player_list[i].hands_played) + ",", end="")
                print(str(self.player_list[i].num_doubles) + ",", end="")
                print(str(self.player_list[i].num_splits) + ",", end="")
                print(str(self.player_list[i].total_wagered) + ",", end="")
                print("")
                sys.stdout = sys.__stdout__


    def finalizeStatistics(self):
        for i in range(len(self.player_list)):
            # Checkpoint this player's statistics
            relativePath = '/results/' + str(self.player_list[i].name) + '.csv'
            resultsPath = self.dirPath + relativePath
            if os.path.isfile(resultsPath):
                sys.stdout = open(resultsPath, 'a')
            else:
                sys.stdout = open(resultsPath, 'w')
            # Print comma separated values that we care about
            print(str(self.player_list[i].chips) + ",", end="")
            print(str(self.player_list[i].shoes_played) + ",", end="")
            print(str(self.player_list[i].hands_played) + ",", end="")
            print(str(self.player_list[i].num_doubles) + ",", end="")
            print(str(self.player_list[i].num_splits) + ",", end="")
            print(str(self.player_list[i].total_wagered) + ",", end="")
            print("")
            print("# End of run")
            sys.stdout = sys.__stdout__


    def simulateHand(self):
        if DEBUG:
            print("Starting a new hand...")

        # Get bets and reset players
        for i in range(len(self.player_list)):
            self.player_list[i].resetPlayer()
            self.setBet(i)
        self.dealer.resetPlayer()

        self.dealStartingCards()
        # First check for insurance & everyone's blackjack
        self.checkForInsuranceAndBlackjack()

        for i in range(len(self.player_list)):
            # Each player remaining plays their hand to completion
            if True in self.player_list[i].active_list:
                self.curr_game.position = i
                self.playHand(i)
        if DEBUG:
            self.printCurrGameState()
        self.curr_game.position = len(self.player_list)
        if DEBUG:
            print("")
        self.playDealer()
        if DEBUG:
            self.printCurrGameState()
        self.payoutWinners()
        if DEBUG:
            self.printStandings()


    def printStandings(self):
        if self.interactive_mode:
            for player in self.player_list:
                print(player.name, end="") 
                self.printNumSpaces(14 - len(player.name))
                print(": " + str(player.chips) + "  (after betting " + str(player.bet) + ")")


    def payoutWinners(self):
        for i in range(len(self.player_list)):
            for j in range(len(self.player_list[i].hands)):
                if self.player_list[i].active_list[j]:
                    pVal = self.getOptimalValue(self.player_list[i].hands[j])
                    dVal = self.getOptimalValue(self.dealer.hands[0])
                    if pVal > 21:
                        # Bust
                        pass
                    elif pVal <= 21:
                        # Player is still in play, check if push first
                        if pVal == dVal:
                            # Push
                            if self.player_list[i].double_list[j]:
                                self.payoutPlayer(i, self.FACTOR_PUSH * 2)
                            else:
                                self.payoutPlayer(i, self.FACTOR_PUSH)
                        elif pVal > dVal or dVal > 21:
                            # Winner!
                            if self.player_list[i].double_list[j]:
                                self.payoutPlayer(i, self.FACTOR_DOUBLE)
                            else:
                                self.payoutPlayer(i, self.FACTOR_WIN)
                        else:
                            # Not a winner
                            pass
                self.player_list[i].active_list[j] = False


    def playDealer(self):
        # Play the dealer based on S17/H17 rules
        if self.stand_on_s17:
            while self.getOptimalValue(self.dealer.hands[0]) < 17:
                self.dealer.hands[0].append(self.curr_game.shoe.popCard())
        else:
            while self.getOptimalValue(self.dealer.hands[0]) < 17 or (self.isHandSoft(self.dealer.hands[0]) and self.getOptimalValue(self.dealer.hands[0]) == 17):
                self.dealer.hands[0].append(self.curr_game.shoe.popCard())


    def setBet(self, position):
        if self.player_adjust_betting_list[position] == "HiLo":
            if self.curr_game.hilo_true_count > 1: 
                betAmount = min(self.min_bet + (self.min_bet * self.curr_game.hilo_true_count * 2), self.min_bet * 12)
            else:
                betAmount = self.min_bet
        elif self.player_adjust_betting_list[position] == "Felt":
            if self.curr_game.felt_true_count > 1: 
                betAmount = min(self.min_bet + (self.min_bet * self.curr_game.felt_true_count * 1), self.min_bet * 12)
            else:
                betAmount = self.min_bet
        else:
            betAmount = self.min_bet
        if DEBUG:
            if self.player_adjust_betting_list[position] == "HiLo":
                print(str(self.player_list[position].name) + " betting " + str(betAmount) + " on a TC of " + str(self.curr_game.hilo_true_count) + "(" + str(self.curr_game.hilo_run_count) + ")")
            elif self.player_adjust_betting_list[position] == "Felt":
                print(str(self.player_list[position].name) + " betting " + str(betAmount) + " on a TC of " + str(self.curr_game.felt_true_count) + "(" + str(self.curr_game.felt_run_count) + ")")
        self.player_list[position].bet = betAmount
        self.player_list[position].chips -= betAmount
        self.player_list[position].total_wagered += betAmount
        


    """
    " This function will return the strategy lookup index for the dealer's face-up card
    "
    " 2-9  -> 2-9
    " 10-K -> 10
    " A    -> A
    """
    def getDealerIndex(self):
        rank = self.dealer.hands[0][0].rank
        if rank < 10:
            return rank
        elif rank == 14: # Ace
            return 11 # Ace mapping
        else:
            return 10 # 10 through King


    """
    " This function will play out the hand(s) for a  player until they Stand or
    " have a value >= 21.  If the player splits, then this function recurses
    " until the player no longer splits or the max number of hands has been reached.
    "
    " Parameters:
    "   position - the index within the simulation's player_list
    "   hand_idx - the index of the hand the player is playing
    """
    def playHand(self, position, hand_idx = 0):
        while self.getOptimalValue(self.player_list[position].hands[hand_idx]) < 21:
            # Deal first card if this is a new hand from a split
            if len(self.player_list[position].hands[hand_idx]) == 1:
                # Check if this was a split of Aces
                if self.player_list[position].hands[hand_idx][0].rank == 14:
                    if DEBUG:
                        print("Dealing second and only card for the split ace.")
                    self.player_list[position].hands[hand_idx].append(self.curr_game.shoe.popCard())
                    break
                if DEBUG:
                    print("Dealing second card for new hand.")
                self.player_list[position].hands[hand_idx].append(self.curr_game.shoe.popCard())
                # Check for blackjack
                if self.isBlackjack(position, hand_idx):
                    if DEBUG:
                        print(self.player_list[position].name + " gets a blackjack on hand " + str(hand_idx))
                    self.payoutPlayer(position, self.FACTOR_BLACKJACK)
                    break
            # CHECK AND HANDLE SPLIT ACTION
            if self.player_strategy_list[position][self.getStratKeyFromHand(self.player_list[position].hands[hand_idx])][self.getDealerIndex()][0] == self.ACTION_SPLIT:
                if DEBUG:
                    print(self.player_list[position].name + " chooses to Split...")
                if len(self.player_list[position].hands) < self.num_splits+1:
                    # Player can execute split, move second card to a new hand
                    self.player_list[position].num_splits += 1
                    self.player_list[position].hands.append([])
                    self.player_list[position].active_list.append(True)
                    self.player_list[position].double_list.append(False)
                    self.player_list[position].hands[-1].append(self.player_list[position].hands[hand_idx][1])
                    del self.player_list[position].hands[hand_idx][1]
                    # Player increases his wager
                    currBet = self.player_list[position].bet
                    self.player_list[position].chips -= currBet
                    self.player_list[position].total_wagered += currBet
                else:
                    if DEBUG:
                        print("Player cannot split, follow-up action...")
                    # Player cannot execute split, lookup decision as a hard value
                    if self.player_strategy_list[position][self.getHardStratKeyFromHand(self.player_list[position].hands[hand_idx])][self.getDealerIndex()][0] == self.ACTION_STAND:
                        if DEBUG:
                            print("Player chooses to Stand.")
                        break
                    elif self.player_strategy_list[position][self.getHardStratKeyFromHand(self.player_list[position].hands[hand_idx])][self.getDealerIndex()][0] == self.ACTION_HIT:
                        if DEBUG:
                            print("Player chooses to Hit.")
                        self.player_list[position].hands[hand_idx].append(self.curr_game.shoe.popCard())
                    elif self.player_strategy_list[position][self.getHardStratKeyFromHand(self.player_list[position].hands[hand_idx])][self.getDealerIndex()][0] == self.ACTION_SURRENDER:
                        if DEBUG:
                            print("Player chooses to Surrender.")
                        """
                        " Player surrenders 
                        "   - if surrender is not allowed, take followup decision
                        "   - if this is her only hand, payout and set her inactive
                        "   - if she has multiple hands, payout and remove hand as necessary
                        """
                        if not self.surrender_allowed or len(self.player_list[position].hands[hand_idx]) > 2:
                            # At this point, only stand or hit are remaining possible options
                            if self.player_strategy_list[position][self.getHardStratKeyFromHand(self.player_list[position].hands[hand_idx])][self.getDealerIndex()][1] == self.ACTION_STAND:
                                break
                            else:
                                # Hit
                                if DEBUG:
                                    print("Player forced to hit.")
                                self.player_list[position].hands[hand_idx].append(self.curr_game.shoe.popCard())
                        else:
                            # TODO Handle surrender
                            pass
            # CHECK AND HANDLE DOUBLE ACTION
            elif self.player_strategy_list[position][self.getStratKeyFromHand(self.player_list[position].hands[hand_idx])][self.getDealerIndex()][0] == self.ACTION_DOUBLE:
                if DEBUG:
                    print(self.player_list[position].name + " chooses to Double...")
                if len(self.player_list[position].hands[hand_idx]) == 2:
                    if DEBUG:
                        print(self.player_list[position].name + " hand before: ")
                        for card in self.player_list[position].hands[hand_idx]:
                            print(str(card))
                    self.player_list[position].hands[hand_idx].append(self.curr_game.shoe.popCard())
                    if DEBUG:
                        print(self.player_list[position].name + " hand after: ")
                        for card in self.player_list[position].hands[hand_idx]:
                            print(str(card))
                    self.player_list[position].num_doubles += 1
                    self.player_list[position].double_list[hand_idx] = True
                    self.player_list[position].chips -= self.player_list[position].bet
                    self.player_list[position].total_wagered += self.player_list[position].bet
                    break # No more actions after a double
                else:
                    if DEBUG:
                        print("Player cannot double, follow-up action...")
                    # Player cannot execute double, lookup follow-up decision
                    if self.player_strategy_list[position][self.getStratKeyFromHand(self.player_list[position].hands[hand_idx])][self.getDealerIndex()][1] == self.ACTION_STAND:
                        if DEBUG:
                            print("Player chooses to Stand.")
                        break
                    else: 
                        # Only remaining action is to hit
                        if DEBUG:
                            print("Player chooses to Hit.")
                        self.player_list[position].hands[hand_idx].append(self.curr_game.shoe.popCard())
            # CHECK AND HANDLE STAND ACTION
            elif self.player_strategy_list[position][self.getStratKeyFromHand(self.player_list[position].hands[hand_idx])][self.getDealerIndex()][0] == self.ACTION_STAND:
                if DEBUG:
                    print(self.player_list[position].name + " chooses to Stand.")
                break
            # CHECK AND HANDLE HIT ACTION
            elif self.player_strategy_list[position][self.getStratKeyFromHand(self.player_list[position].hands[hand_idx])][self.getDealerIndex()][0] == self.ACTION_HIT:
                if DEBUG:
                    print(self.player_list[position].name + " chooses to Hit...")
                    print(self.player_list[position].name + " hand before: ")
                    for card in self.player_list[position].hands[hand_idx]:
                        print(str(card))
                self.player_list[position].hands[hand_idx].append(self.curr_game.shoe.popCard())
                if DEBUG:
                    print(self.player_list[position].name + " hand after: ")
                    for card in self.player_list[position].hands[hand_idx]:
                        print(str(card))
            elif self.player_strategy_list[position][self.getStratKeyFromHand(self.player_list[position].hands[hand_idx])][self.getDealerIndex()][0] == self.ACTION_SURRENDER:
                if not self.surrender_allowed or len(self.player_list[position].hands[hand_idx]) > 2:
                    # At this point, only stand or hit are remaining possible options
                    if self.player_strategy_list[position][self.getStratKeyFromHand(self.player_list[position].hands[hand_idx])][self.getDealerIndex()][1] == self.ACTION_STAND:
                        if DEBUG:
                            print(self.player_list[position].name + " chooses to Surrender. Unable -> Stand.")
                        break
                    else:
                        # Hit
                        if DEBUG:
                            print(self.player_list[position].name + " chooses to Surrender. Unable -> Hit.")
                        self.player_list[position].hands[hand_idx].append(self.curr_game.shoe.popCard())
                else:
                    if DEBUG:
                        print(self.player_list[position].name + " chooses to Surrender.")
                    self.player_list[position].active_list[hand_idx] = False
                    self.payoutPlayer(position, self.FACTOR_SURRENDER)

        # Finished handling actions for the hand, if a new hand was split off then we must play that one next
        numHands = len(self.player_list[position].hands)
        handsRemain = False
        if numHands > hand_idx+1 and len(self.player_list[position].hands[hand_idx+1]) == 1:
            handsRemain = True
        if handsRemain:
            if DEBUG:
                print("Detected split, starting hand number " + str(hand_idx+1))
            self.playHand(position, hand_idx+1)
        return


    def isBlackjack(self, position, hand_idx):
        if self.getOptimalValue(self.player_list[position].hands[hand_idx]) == 21 and len(self.player_list[position].hands[hand_idx]) == 2:
            return True
        return False


    def checkForInsuranceAndBlackjack(self):
        dealerHasAceUp = self.dealer.hands[0][0].rank == 14
        insurance_list = []

        # First handle insurance if necessary
        if dealerHasAceUp:
            for i in range(len(self.player_list)):
                if self.player_list[i].wantsInsurance():
                    # Player decided to opt for insurance
                    if DEBUG:
                        print(str(self.player_list[i].name) + " decided to take insurance.")
                    insurance_list.append(True)
                    self.player_list[i].chips -= self.player_list[i].bet / 2.0
                    self.player_list[i].total_wagered += self.player_list[i].bet / 2.0
                else:
                    if DEBUG:
                        print(str(self.player_list[i].name) + " decided NOT to take insurance.")
                    insurance_list.append(False)

        if self.getOptimalValue(self.dealer.hands[0]) == 21 and len(self.dealer.hands[0]) == 2:
            # Poor players. The dealer has blackjack.
            for i in range(len(self.player_list)):
                self.player_list[i].active_list = [False]
                if dealerHasAceUp:
                    if insurance_list[i]:
                        # This player wins on their insurance bet
                        self.payoutPlayer(i, self.FACTOR_WIN) 
                    elif self.getOptimalValue(self.player_list[i].hands[0]) == 21 and len(self.player_list[i].hands[0]) == 2:
                        # This player has blackjack at least for a push!
                        self.player_list[i].active_list[0] = False
                        self.payoutPlayer(i, self.FACTOR_PUSH)
                else:
                    if self.getOptimalValue(self.player_list[i].hands[0]) == 21 and len(self.player_list[i].hands[0]) == 2:
                        self.payoutPlayer(i, self.FACTOR_PUSH)
        else:
            # The dealer does not have blackjack
            for i in range(len(self.player_list)):
                if self.getOptimalValue(self.player_list[i].hands[0]) == 21 and len(self.player_list[i].hands[0]) == 2:
                    # This player has blackjack!
                    self.player_list[i].active_list[0] = False
                    self.payoutPlayer(i, self.FACTOR_BLACKJACK)


    """
    " TODO
    """
    def getDecision(self, position, card_list, is_follow_up):
        if is_follow_up:
            idx = 0
        else:
            idx = 1
        if self.player_indexing_list[position]:
            if self.player_list[position].player_index_list[self.getStratKeyFromHand(card_list)]:
                is_positive = self.player_list[position].player_index_list[self.getStratKeyFromHand(card_list)][1] >= 0:
                # Check that the count is higher than a positive index, or lower than a negative one
                if is_positive and self.curr_game.true_count >= self.player_list[position].player_index_list[self.getStratKeyFromHand(card_list)][1]:
                    return self.player_list[position].player_index_list[self.getStratKeyFromHand(card_list)][0]:
                elif not is_positive and self.curr_game.true_count < self.player_list[position].player_index_list[self.getStratKeyFromHand(card_list)][1]:
                    return self.player_list[position].player_index_list[self.getStratKeyFromHand(card_list)][0]:
        return self.player_strategy_list[position][self.getStratKeyFromHand(self.player_list[position].hands[hand_idx])][self.getDealerIndex()][idx]
                    
    

    """
    " This function will produce the key necessary to look up the proper choice in the strategy dictionary.
    " The following examples show how the key is formatted and prioritized:
    "
    "   Pair of cards, i.e. 6 and 6 = "p6"
    "   Soft value, i.e. 4 and King = "s15"
    "   Hard value, i.e. 5 and Jack = "15"
    """
    def getStratKeyFromHand(self, card_list):
        if len(card_list) == 2:
            retRank0 = card_list[0].rank
            retRank1 = card_list[1].rank
            if retRank0 == 14:
                retRank0 = "A"
            elif retRank0 >= 10:
                retRank0 = "10"
            else:
                retRank0 = str(retRank0)
            if retRank1 == 14:
                retRank1 = "A"
            elif retRank1 >= 10:
                retRank1 = "10"
            else:
                retRank1 = str(retRank1)
            if retRank0 == retRank1:
                return "p" + retRank0
        if self.isHandSoft(card_list):
            return "s" + str(self.getOptimalValue(card_list))
        else:
            return str(self.getOptimalValue(card_list))


    """
    " This function will produce the key necessary to look up the proper choice in the strategy dictionary
    " for hard values only.  This is to be used as the secondary action if a split is not allowed for
    " whatever reason.
    """
    def getHardStratKeyFromHand(self, card_list):
        if len(card_list) != 2:
            print("Error: calling getHardStratKeyFromHand() with a non-pair hand!")
        return str(self.getOptimalValue(card_list))


    """
    " This function returns whether or not the hand is soft, which means the hand contains an Ace
    " using a value of 11 without going over 21
    """
    def isHandSoft(self, card_list):
        return self.getOptimalValue(card_list) != self.getMinValue(card_list)


    """
    " This function will return the value of the hand that is closest to 21 without going over. If the
    " total is over 21, the Aces will count as 1 if that matters. Soft hands should be checked with
    " BjSimulation.isHandSoft()
    """
    def getOptimalValue(self, card_list):
        sum = 0
        hasAce = False
        for card in card_list:
            if card.rank == 14:
                sum += 1
                hasAce = True
            elif card.rank >= 10:
                sum += 10
            else:
                sum += card.rank
        if hasAce and (sum + 10) <= 21:
            sum += 10 
        return sum


    def getMinValue(self, card_list):
        sum = 0
        for card in card_list:
            if card.rank == 14:
                sum += 1
            elif card.rank >= 10:
                sum += 10
            else:
                sum += card.rank
        return sum


    def payoutPlayer(self, position, factor):
        if DEBUG:
            print("Paying " + self.player_list[position].name + " " + str(factor))
        self.player_list[position].chips += (self.player_list[position].bet * factor)


    def dealStartingCards(self):
        if DEBUG:
            print("Dealing starting cards...")
        # Deal the first card to each player in order then the dealer
        for i in range(len(self.player_list)):
            self.player_list[i].hands[0].append(self.curr_game.shoe.popCard())
        # Deal the first card to the dealer
        self.dealer.hands[0].append(self.curr_game.shoe.popCard())
        # Deal the second card to each player in order then the dealer
        for i in range(len(self.player_list)):
            self.player_list[i].hands[0].append(self.curr_game.shoe.popCard())
        # Deal the second card to the dealer
        self.dealer.hands[0].append(self.curr_game.shoe.popCard())

        if DEBUG:
            self.printCurrGameState()


    """
    " This function will print an ASCII representation of curr_game, spanning < 80 characters
    """
    def printCurrGameState(self):
        print("################################################################################")
        print("################################ Current State #################################")
        print("################################################################################")
        print("Shoe: " + str(self.curr_game.shoe.cards_remaining) + "/" + str(self.curr_game.shoe.num_decks * 52) + " felt(" + str(self.curr_game.felt_true_count) + "|" + str(self.curr_game.felt_run_count) + ") hilo(" + str(self.curr_game.hilo_true_count) + "|" + str(self.curr_game.hilo_run_count) + ")")
        print("")
        print("                                    Dealer")
        print("                                    ", end="")
        for i in range(len(self.dealer.hands[0])):
            if i == 1 and not self.isDealerPlaying():
                print("XX ", end="")
            else:
                print(str(self.dealer.hands[0][i]) + " ", end="")
        print("")
        # Print from right to left like a real casino
        for i in range(6, 0, -1):
            if i > self.num_players:
                sys.stdout.write(".")
                self.printNumSpaces(12)
            else:
                player_index = i-1
                left_pad = (13 - len(self.player_list[player_index].name)) / 2
                right_pad = 13 - left_pad - len(self.player_list[player_index].name)
                sys.stdout.write (".")
                self.printNumSpaces(left_pad)
                sys.stdout.write(self.player_list[player_index].name)
                self.printNumSpaces(right_pad-1)
        print(" .")
        # Print the hands vertically for each player, this comprehension finds the largest hand
        currLists = []
        for i in range(len(self.player_list)):
            for j in range(len(self.player_list[i].hands)):
                currLists.append(self.player_list[i].hands[j])
        for i in range(max([len(list) for list in currLists])):
            self.printNumSpaces(13 * (6 - len(self.player_list)))
            for j in range(len(self.player_list)-1, -1, -1):
                # Print each hand for this player if applicable
                if len(self.player_list[j].hands) == 1:
                    if len(self.player_list[j].hands[0]) > i:
                        self.printNumSpaces(13 - 5 - len(str(self.player_list[j].hands[0][i])))
                        sys.stdout.write(str(self.player_list[j].hands[0][i]))
                        self.printNumSpaces(5)
                    else:
                        print("             ", end="")
                else:
                    concatCards = " "
                    for k in range(len(self.player_list[j].hands)):
                        # If there are splits, let's just pring them concatenated together
                        if len(self.player_list[j].hands[k]) > i:
                            # Three characters apiece. Check for length to know
                            if len(str(self.player_list[j].hands[k][i])) == 3:
                                concatCards += str(self.player_list[j].hands[k][i])
                            else:
                                concatCards += " " + str(self.player_list[j].hands[k][i])
                        else:
                            concatCards += "   "
                    sys.stdout.write(concatCards)
                    self.printNumSpaces(12-len(concatCards))
            print("")
        print("")

            
        print("################################################################################")


    def printNumSpaces(self, num_spaces):
        for i in range(num_spaces):
            sys.stdout.write(" ")


    def isDealerPlaying(self):
        if self.curr_game.position == self.num_players:
            return True
        else:
            return False


        

class GameState(object):
    """
    " Holds the state of the game
    " shoe             : Holds all of the decks and is used to deal the cards
    " cut_card         : Holds the position of a virtual cut card. Dealing passed
    "                  :   the cut card indicates a reshuffle. The range is decided
    "                  :   by the pen_min and pen_max of the BjSimulation
    " position         : Current position of the player playing. The first player is
    "                  : in the zero'th position. The dealer is the last position,
    "                  : which is equivalent to the number of players
    " hilo_run_count      : The total running count for the shoe
    " hilo_true_count  : The total running count for the shoe divided by the number
    "                  :   of decks. This is the count that should be used to
    "                  :   determine bet amount and decisions in the hilo system.
    " felt_true_count  : The total running count for the shoe divided by the number
    "                  :   of decks. This is the count that should be used to
    "                  :   determine bet amount and decisions in the felt system.
    " num_decks        : The number of decks in the shoe
    """

    def keepCount(self, func):
        def wrapped(*args, **kwargs):
            card = func(*args, **kwargs)
            if DEBUG_COUNT:
                print("Popping " + str(card))
            # FELT SYSTEM
            if card.rank < 3:
                self.felt_run_count += 1
                self.felt_true_count = self.felt_run_count / (1 + (self.shoe.cards_remaining / 52))
                #self.felt_true_count = int((self.felt_true_count + 0.5) / 1) # Round
            elif card.rank < 7:
                self.felt_run_count += 2
                self.felt_true_count = self.felt_run_count / (1 + (self.shoe.cards_remaining / 52))
                #self.felt_true_count = int((self.felt_true_count + 0.5) / 1) # Round
            elif card.rank == 7:
                self.felt_run_count += 1
                self.felt_true_count = self.felt_run_count / (1 + (self.shoe.cards_remaining / 52))
                #self.felt_true_count = int((self.felt_true_count + 0.5) / 1) # Round
            elif card.rank < 10:
                self.felt_true_count = self.felt_run_count / (1 + (self.shoe.cards_remaining / 52))
                #self.felt_true_count = int((self.felt_true_count + 0.5) / 1) # Round
            else:
                self.felt_run_count -= 2
                self.felt_true_count = self.felt_run_count / (1 + (self.shoe.cards_remaining / 52))
                #self.felt_true_count = int((self.felt_true_count + 0.5) / 1) # Round
            if DEBUG_COUNT:
                print("frc: " + str(self.felt_run_count))
                print("ftc: " + str(self.felt_true_count))
            # HILO SYSTEM
            if card.rank < 7:
                self.hilo_run_count += 1
                self.hilo_true_count = self.hilo_run_count / (1 + (self.shoe.cards_remaining / 52))
                #self.hilo_true_count = int((self.hilo_true_count + 0.5) / 1) # Round
            elif card.rank < 10:
                self.hilo_true_count = self.hilo_run_count / (1 + (self.shoe.cards_remaining / 52))
                #self.hilo_true_count = int((self.hilo_true_count + 0.5) / 1) # Round
            else:
                self.hilo_run_count -= 1
                self.hilo_true_count = self.hilo_run_count / (1 + (self.shoe.cards_remaining / 52))
                #self.hilo_true_count = int((self.hilo_true_count + 0.5) / 1) # Round
            if DEBUG_COUNT:
                print("hrc: " + str(self.hilo_run_count))
                print("htc: " + str(self.hilo_true_count))
            return card
        return wrapped

    def __init__(self, num_decks, pen_min, pen_max):
        self.shoe = Shoe(num_decks)
        self.position = -1
        self.hilo_run_count = 0
        self.felt_run_count = 0
        self.hilo_true_count = 0
        self.felt_true_count = 0
        self.num_decks = num_decks
        # Measure from the back of the Shoe so we can compare with the number of Cards remaining
        self.cut_card = (100 - random.randint(pen_min, pen_max)) * num_decks * 52 / 100
        if DEBUG:
            print("Given pen range (" + str(pen_min) + ", " + str(pen_max) + ") the randomly chosen cut_card is: " + str(self.cut_card) + " which is " + str((num_decks * 52 - self.cut_card) * 100 / (num_decks * 52)) + " percent deep.")
        random.shuffle(self.shoe.cards)
        self.shoe.popCard = self.keepCount(self.shoe.popCard)


            

class Player(object):
    """
    " Holds information about a current player
    "
    " Attributes:
    "   position      - seat at the table
    "                   0: first seat
    "   chips         - total chips not currently at stake
    "   strategy      - mapping for decisions
    "   name          - optional string for the player's name
    "   hands         - list of currently held cards, multiple if splits
    "   double_list   - list of booleans indicating a double bet 
    "   bet           - the player's current bet
    "   hands_played  - the number of hands played so far. a split hand is still
    "                   counted as only a single hand 
    "   shoes_played  - the number of shoes seen by the player so far
    "   num_doubles   - the number of total double down bets
    "   num_splits    - the number of total splits
    "   total_wagered - the total amount wagered so far
    """

    def __init__(self, position, strategy, starting_chips, name = ""):
        self.position = position
        self.chips = starting_chips
        self.strategy = strategy
        self.name = name
        self.hands = [[]]
        self.active_list = [False]
        self.double_list = []
        self.bet = 0
        self.hands_played = 0
        self.shoes_played = 0
        self.num_doubles = 0
        self.num_splits = 0
        self.total_wagered = 0

    def resetPlayer(self):
        self.hands = [[]]
        self.active_list = [True]
        self.double_list = [False]
        self.bet = 0

    def wantsInsurance(self):
        return False

