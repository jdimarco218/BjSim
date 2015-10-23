class Card(object):
    """ 
    " Represents a standard playing card.
    " 
    " Attributes:
    "     suit: integer 0-3
    "     rank: integer 2-14
    "
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ["None", "None", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    suit_names_short = ["C", "D", "H", "S"]
    rank_names_short = ["None", "None", "2", "3", "4", "5", "6", "7",
                        "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit=2, rank=0, print_short = True):
        self.suit = suit
        self.rank = rank
        self.print_short = print_short

    def __str__(self, override = False):
        """ Returns a human-readable string representation."""
        if not self.print_short or override:
            return '%s of %s' % (Card.rank_names[self.rank],
                                 Card.suit_names[self.suit])
        else:
            return '%s%s' % (Card.rank_names_short[self.rank],
                             Card.suit_names_short[self.suit])

    def __cmp__(self, other):
        """
        " Compares this card to other by rank only.
        "  
        " Returns 1 if this > other, -1 if this < other, 0 if equal
        "
        """
        return cmp(self.rank, other.rank)
