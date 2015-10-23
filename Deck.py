import random
from Card import Card

class Deck(object):
    """
    " Represents a deck of standard playing cards.
    "
    " Attributes:
    "     cards: list of playing cards
    """

    def __init__(self, num_decks):
        self.cards = []
        for deck in range(num_decks):
            for suit in range(4):
                for rank in range(2, 15):
                    card = Card(suit, rank)
                    self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle(self):
        """ Shuffles the cards in this deck. """
        random.shuffle(self.cards)

    def popCard(self, i=0):
        """  Removes and returns a card from the deck. First card default"""
        return self.cards.pop(i)
