import random
from .card import Card


class Deck:
    '''Deck of the cards for the BlackJack

    By default initializing with 52 shuffled cards

    Attributes
    ----------
    suits : set
        set of four suits of cards
    values : dict
        dictionary with all possible cards ranks and their values
    cards : list
        list of all cards in the deck

    Methods
    -------
    add_card(card=Card)
        adding a card to the deck

    shuffle_deck()
        shuffling a deck using random.shuffle

    draw_card()
        drawing a card by poping a card from the deck and returning it

    fill_deck()
        filling a deck with 52 cards by looping through suits and values
    '''

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
              'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self):
        self.cards = []
        self.fill_deck()
        self.shuffle_deck()

    def __str__(self):
        return f'Deck contains: {self.cards}'

    def add_card(self, card=Card):
        self.cards.append(card)

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if (len(self.cards) > 0):
            return self.cards.pop()
        else:
            print('Can\' draw, deck is empty')

    def fill_deck(self):
        for suit in self.suits:
            for key, value in self.values.items():
                card = Card(suit, key, value)
                self.add_card(card)
