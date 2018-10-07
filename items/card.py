class Card:
    '''Representation of the single card in the BlackJack game

    Each Card has the information about it suit, rank and value

    Attributes
    ----------
    suit : str
        card suit
    rank : str
        card rank
    value : int
        card value
    '''

    def __init__(self, suit='', rank='', value=0):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit}'
