class Player:
    '''Player for a BlackJack game

    Player has a name and a balance with ability to withdraw and add money 

    Attributes
    ----------
    name : str
        the name of the player
    balance : int
        the initial amount of money on the balance

    Methods
    -------
    withdraw_money(amount=0)
        trying to subtract passed amount from the balance
        printing an update balance if succeeded or an error if balance was too low for substaction

    add_money(amount=0)
        adding passed amount to the player balance and printing updated balance

    print_balance()
        printing the balance of the player
    '''

    def __init__(self, name='', balance=0):
        self.name = name
        self.balance = balance

    def withdraw_money(self, amount=0):
        is_enough = self.balance >= amount

        if (is_enough):
            self.balance -= amount
            self.print_balance()
        else:
            print('You don\'t have enough money! \n')

        return is_enough

    def add_money(self, amount=0):
        self.balance += amount
        self.print_balance()

    def print_balance(self):
        print(f'\nYour new balance is {self.balance}. \n')
