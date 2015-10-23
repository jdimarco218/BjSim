import random
from Card import Card
from Deck import Deck

class Shoe(object):
    """
    " Represents a blackjack shoe containing multiple Decks.
    "
    " Attributes:
    "     num_decks: starting number of decks
    "     cards: list of playing cards
    "     cards_remaining: number of remaining cards
    """

    def __init__(self, num_decks):
        self.cards = []
        self.num_decks = num_decks
        self.cards_remaining = 0
        for deck in range(num_decks):
            for suit in range(4):
                for rank in range(2, 15):
                    card = Card(suit, rank)
                    self.cards.append(card)
                    self.cards_remaining += 1

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle(self):
        """ Shuffles the cards in this Shoe. """
        random.shuffle(self.cards)

    def popCard(self, i=0):
        """  Removes and returns a card from the deck. First card default"""
        if self.cards_remaining > 0:
            self.cards_remaining -= 1
            return self.cards.pop(i)
        else:
            print "Error: no cards left to pop!"
            return None

