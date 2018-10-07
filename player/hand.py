from items.card import Card


class Hand:
    '''Hand of the player or dealer in BlackJack

    Hand of cards with total values and aces count 

    Attributes
    ----------
    values : int
        total values of the cards in the hand
    aces : int
        the amount of aces in the hand

    Methods
    -------
    add_card(card=Card)
        adding a card to the hand by updating values and aces amount if it's an ace

    update_values(value=0)
        updating the hand values with the passed value and calling adjust_for_aces

    adjust_for_aces()
        checking if hand values higher then 21 and, if hand contains any aces, 
        lowering values by 10 for each ace, till values became lower then 21
    '''

    def __init__(self):
        self.values = 0
        self.aces = 0

    def add_card(self, card=Card):
        if (card.rank == 'Ace'):
            self.aces += 1
        self.update_values(card.value)

    def update_values(self, value=0):
        self.values += value
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.values > 21 and self.aces > 0:
            self.values -= 10
            self.aces -= 1
