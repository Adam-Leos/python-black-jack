from player.player import Player
from items.deck import Deck
from blackjack.blackjack import BlackJack

# Creating a player
player = Player('Adam', 1000)
# Creating a deck
deck = Deck()
# Creating a game
game = BlackJack(deck, player)
# And starting it
game.start_game()
