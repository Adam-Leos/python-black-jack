from player.player import Player
from player.hand import Hand
from items.deck import Deck


class BlackJack:
    '''Simplified game representation for one player, playing against dealer.

    Dealer plays with the passed deck against passed player. 
    Player should set a bet from his balance and game ends if player lose all money. 
    Everyone start with two cards in hand. Player able to see only one card in dealer hand.
    Player can draw more cards or pass and let a dealer draw.
    Dealer is drawing only if has less then 17 points.
    Anyone who has more then 21 point is bust.
    If both have passed and not busted, winner is a score, closest to 21 points.

    Attributes
    ----------
    deck : Deck
        list of cards in the game
    player : Player
        player, playing against dealer
    is_game_active : bool
        equals to True till game is running, repeatedly starting new round till the end of the game
    bet : int
        bet set by Player

    Methods
    -------
    start_game()
        starting a game with the loop, continuesly starting new round till end of the game

    start_new_round()
        starting new round with setting bet, initializing hands and asking for an additional draw
        after draws determining a winner and ending the game

    set_bet()
        Asking player for the bet to set. 
        He should enter a positive number and should have this amount on his balance

    draw_card(is_hidden=bool)
        drawing a card from the deck and returning it.
        Printing this card unless is_hidden was set to True

    init_hands()
        initializing hands of the dealer and the player, 
        by creating empty hands and drawing two cards for each.
        Printing each hands, except first draw of the dealer.

    check_is_bust(hand=Hand)
        player is busted if his hand values higher of 21

    determine_winner(is_player_bust=bool)
        Determining a winner. If someone if bust, then another win.
        If none, then finding out who's score is closer to 21 and calling him a winner.

    ask_player_confirmation(message=str)
        Asking player confirmation with the passed message. Returning boolean.

    end_round(winner=str)
        ending a round, if player won, adding money to his account 
        and if he still has money, asking for continue playing

    end_game()
        ending the game, setting is_game_active to False to prevent new rounds
        and printing a farewell message

    '''

    def __init__(self, deck=Deck, player=Player):
        self.deck = deck
        self.player = player
        self.is_game_active = True
        self.bet = 0

    def start_game(self):
        while self.is_game_active:
            self.start_new_round()

    def start_new_round(self):
        is_player_bust = False
        self.set_bet()
        self.init_hands()

        # player able to draw more cards, one by one, by confirming message
        while not is_player_bust:
            is_to_draw_card = self.ask_player_confirmation(
                'Do you want to draw one more card?')

            if (is_to_draw_card):
                self.player_hand.add_card(self.draw_card())
                is_player_bust = self.check_is_bust(self.player_hand)
            else:
                break

        # dealer is automatically drawing till he'll get 17 or higher
        while self.dealer_hand.values < 17:
            self.dealer_hand.add_card(self.draw_card())

        winner = self.determine_winner(is_player_bust)
        self.end_round(winner)

    def set_bet(self):
        while True:
            try:
                player_bet = int(input('Make your bet: '))
            except:
                print('Bet should be a positive number')
            else:
                if (self.player.withdraw_money(player_bet)):
                    self.bet = player_bet
                    print(f'Bet is set ({player_bet})')
                    break

    def draw_card(self, is_hidden=False):
        card = self.deck.draw_card()
        message = 'Hidden draw' if is_hidden else f'{card} with value of {card.value}'

        print(message)
        return card

    def init_hands(self):
        self.dealer_hand = Hand()
        self.player_hand = Hand()

        print('\nDealer initial draw: ')
        self.dealer_hand.add_card(self.draw_card(True))
        self.dealer_hand.add_card(self.draw_card())

        print('\nPlayer initial draw: ')
        self.player_hand.add_card(self.draw_card())
        self.player_hand.add_card(self.draw_card())

    def check_is_bust(self, hand=Hand):
        return hand.values > 21

    # TODO make a tie acceptable...
    def determine_winner(self, is_player_bust=False):
        player_score = self.player_hand.values
        dealer_score = self.dealer_hand.values
        winner = 'dealer'

        print(f'Your score is: {player_score}')
        print(f'Dealer score is: {dealer_score} \n')
        if (not is_player_bust and player_score > dealer_score or dealer_score > 21):
            winner = 'player'

        return winner

    def ask_player_confirmation(self, message=''):
        while True:
            next_move = input(f'\n{message} (\'y\' or \'n\'): ').lower()

            # checking for the first char in input to help with the typo
            if (next_move[0] == 'y' or next_move[0] == 'n'):
                return next_move[0] == 'y'
            else:
                print('Please, enter only \'y\' or \'n\'')

    def end_round(self, winner='dealer'):
        if (winner == 'player'):
            prize = self.bet * 2

            print(f'\nCongratulations, you won {prize}\n')
            self.player.add_money(prize)
        else:
            print(f'\nToo bad, but you lose...\n')

        if (self.player.balance > 0 and self.ask_player_confirmation('\nDo you want to play more?\n')):
            self.start_new_round()
        else:
            self.end_game()

    def end_game(self):
        print(f'\nThanks for a nice game, {self.player.name}...')
        self.is_game_active = False
