# This file contains the input configuration for BjSimulation

HILO = "Hi-Lo"
FELT = "Felt"

interactive_mode = True
num_decks = 6
stand_on_s17 = True
surrender_allowed = False
double_after_split = True
num_splits = 3
penetration_min = 75
penetration_max = 80
rounds_to_play = 1000
store_stats_after_shoe_count = 1
min_bet = 15
print_every_ten_percent = True

# For each player, fill in their starting chips, strategy, and name if wanted
interactive_player_position = 0
basic_strategy = {}
dealer_strategy = []
player_starting_chips_list = [0, 0, 0]
#player_name_list = ["Jeff", "Comp_1"]
#player_name_list = ["Basic"]
#player_name_list = ["HiLo", "Felt", "Basic"]
#player_name_list = ["HiLo", "Basic"]
player_name_list = ["HiLo", "Felt"]
#player_adjust_betting_list = ["HiLo", "Felt", "Basic"]
#player_adjust_betting_list = ["HiLo", "Basic"]
player_adjust_betting_list = ["HiLo", "Felt"]
num_players = len(player_name_list)

basic_strategy_S17 = {
#                              Dealer: 2     3     4     5     6     7     8     9     10    A
                  "2":   [None, None, "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H"],
                  "3":   [None, None, "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H"],
                  "4":   [None, None, "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H"],
                  "5":   [None, None, "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H"],
                  "6":   [None, None, "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H"],
                  "7":   [None, None, "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H"],
                  "8":   [None, None, "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H"],
                  "9":   [None, None, "H",  "DH", "DH", "DH", "DH", "H",  "H",  "H",  "H",  "H"],
                  "10":  [None, None, "DH", "DH", "DH", "DH", "DH", "DH", "DH", "DH", "H",  "H"],
                  "11":  [None, None, "DH", "DH", "DH", "DH", "DH", "DH", "DH", "DH", "DH", "H"],
                  "12":  [None, None, "H",  "H",  "S",  "S",  "S",  "H",  "H",  "H",  "H",  "H"],
                  "13":  [None, None, "S",  "S",  "S",  "S",  "S",  "H",  "H",  "H",  "H",  "H"],
                  "14":  [None, None, "S",  "S",  "S",  "S",  "S",  "H",  "H",  "H",  "H",  "H"],
                  "15":  [None, None, "S",  "S",  "S",  "S",  "S",  "H",  "H",  "H",  "RH", "RH"],
                  "16":  [None, None, "S",  "S",  "S",  "S",  "S",  "H",  "H",  "RH", "RH", "RH"],
                  "17":  [None, None, "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S"],
                  "18":  [None, None, "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S"],
                  "19":  [None, None, "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S"],
                  "20":  [None, None, "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S"],
                  "21":  [None, None, "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S"],

#                              Dealer: 2     3     4     5     6     7    8    9    10   A
                  "s13": [None, None, "H",  "H",  "H",  "DH", "DH", "H", "H", "H", "H", "H"],
                  "s14": [None, None, "H",  "H",  "H",  "DH", "DH", "H", "H", "H", "H", "H"],
                  "s15": [None, None, "H",  "H",  "DH", "DH", "DH", "H", "H", "H", "H", "H"],
                  "s16": [None, None, "H",  "H",  "DH", "DH", "DH", "H", "H", "H", "H", "H"],
                  "s17": [None, None, "H",  "DH", "DH", "DH", "DH", "H", "H", "H", "H", "H"],
                  "s18": [None, None, "S",  "DS", "DS", "DS", "DS", "S", "S", "H", "H", "H"],
                  "s19": [None, None, "S",  "S",  "S",  "S",  "S",  "S", "S", "S", "S", "S"],
                  "s20": [None, None, "S",  "S",  "S",  "S",  "S",  "S", "S", "S", "S", "S"],
#                             Dealer:  2     3     4     5     6     7     8     9     10    A
                  "p2":  [None, None, "PH", "PH", "PH", "PH", "PH", "PH", "H",  "H",  "H",  "H"],
                  "p3":  [None, None, "PH", "PH", "PH", "PH", "PH", "PH", "H",  "H",  "H",  "H"],
                  "p4":  [None, None, "H",  "H",  "H",  "PH", "PH", "H",  "H",  "H",  "H",  "H"],
                  "p5":  [None, None, "D",  "D",  "D",  "D",  "D",  "D",  "D",  "D",  "H",  "H"],
                  "p6":  [None, None, "PH", "PH", "PH", "PH", "PH", "H",  "H",  "H",  "H",  "H"],
                  "p7":  [None, None, "PH", "PH", "PH", "PH", "PH", "PH", "H",  "H",  "H",  "H"],
                  "p8":  [None, None, "PH", "PH", "PH", "PH", "PH", "PH", "PH", "PH", "PH", "PH"],
                  "p9":  [None, None, "P",  "P",  "P",  "P",  "P",  "S",  "P",  "P",  "S",  "S"],
                  "p10": [None, None, "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S"],
                  "pA":  [None, None, "P",  "P",  "P",  "P",  "P",  "P",  "P",  "P",  "P",  "P"],
                 }

basic_strategy_H17 = {
#                              Dealer: 2     3     4     5     6     7     8     9     10    A
                  "2":   [None, None, "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H"],
                  "3":   [None, None, "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H"],
                  "4":   [None, None, "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H"],
                  "5":   [None, None, "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H"],
                  "6":   [None, None, "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H"],
                  "7":   [None, None, "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H"],
                  "8":   [None, None, "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H",  "H"],
                  "9":   [None, None, "H",  "DH", "DH", "DH", "DH", "H",  "H",  "H",  "H",  "H"],
                  "10":  [None, None, "DH", "DH", "DH", "DH", "DH", "DH", "DH", "DH", "H",  "H"],
                  "11":  [None, None, "DH", "DH", "DH", "DH", "DH", "DH", "DH", "DH", "DH", "DH"],
                  "12":  [None, None, "H",  "H",  "S",  "S",  "S",  "H",  "H",  "H",  "H",  "H"],
                  "13":  [None, None, "S",  "S",  "S",  "S",  "S",  "H",  "H",  "H",  "H",  "H"],
                  "14":  [None, None, "S",  "S",  "S",  "S",  "S",  "H",  "H",  "H",  "H",  "H"],
                  "15":  [None, None, "S",  "S",  "S",  "S",  "S",  "H",  "H",  "H",  "RH", "RH"],
                  "16":  [None, None, "S",  "S",  "S",  "S",  "S",  "H",  "H",  "RH", "RH", "RH"],
                  "17":  [None, None, "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "RS"],
                  "18":  [None, None, "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S"],
                  "19":  [None, None, "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S"],
                  "20":  [None, None, "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S"],
                  "21":  [None, None, "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S"],

#                              Dealer: 2     3     4     5     6     7    8    9    10   A
                  "s13": [None, None, "H",  "H",  "H",  "DH", "DH", "H", "H", "H", "H", "H"],
                  "s14": [None, None, "H",  "H",  "H",  "DH", "DH", "H", "H", "H", "H", "H"],
                  "s15": [None, None, "H",  "H",  "DH", "DH", "DH", "H", "H", "H", "H", "H"],
                  "s16": [None, None, "H",  "H",  "DH", "DH", "DH", "H", "H", "H", "H", "H"],
                  "s17": [None, None, "H",  "DH", "DH", "DH", "DH", "H", "H", "H", "H", "H"],
                  "s18": [None, None, "DS", "DS", "DS", "DS", "DS", "S", "S", "H", "H", "H"],
                  "s19": [None, None, "S",  "S",  "S",  "S",  "DS", "S", "S", "S", "S", "S"],
                  "s20": [None, None, "S",  "S",  "S",  "S",  "S",  "S", "S", "S", "S", "S"],
#                             Dealer:  2     3     4     5     6     7     8     9     10    A
                  "p2":  [None, None, "PH", "PH", "PH", "PH", "PH", "PH", "H",  "H",  "H",  "H"],
                  "p3":  [None, None, "PH", "PH", "PH", "PH", "PH", "PH", "H",  "H",  "H",  "H"],
                  "p4":  [None, None, "H",  "H",  "H",  "PH", "PH", "H",  "H",  "H",  "H",  "H"],
                  "p5":  [None, None, "D",  "D",  "D",  "D",  "D",  "D",  "D",  "D",  "H",  "H"],
                  "p6":  [None, None, "PH", "PH", "PH", "PH", "PH", "H",  "H",  "H",  "H",  "H"],
                  "p7":  [None, None, "PH", "PH", "PH", "PH", "PH", "PH", "H",  "H",  "H",  "H"],
                  "p8":  [None, None, "PH", "PH", "PH", "PH", "PH", "PH", "PH", "PH", "PH", "PH"],
                  "p9":  [None, None, "P",  "P",  "P",  "P",  "P",  "S",  "P",  "P",  "S",  "S"],
                  "p10": [None, None, "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S",  "S"],
                  "pA":  [None, None, "P",  "P",  "P",  "P",  "P",  "P",  "P",  "P",  "P",  "P"],
                 }

player_strategy_list = [basic_strategy_S17, basic_strategy_S17, basic_strategy_S17]
