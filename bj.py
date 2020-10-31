'''
Milestone Project 2 - BlackJack
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Ace':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10}

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    def deal_card(self):
        return self.all_cards.pop(0)
    def shuffle(self):
        random.shuffle(self.all_cards)

class Dealer():
    def __init__(self):
        self.all_cards = []
    def add_card(self,card):
        self.all_cards.append(card)

class Player():
    def __init__(self, name):
        self.all_cards = []
        self.name = name
        self.budget = 100
    def add_card(self,card):
        self.all_cards.append(card)
    def modify_budget(self,money):
        self.budget += money

def check_win(d, p, suppress_print):
    '''
    Check who won, player or dealer.
    '''
    s_d = sum_cards(d)
    s_p = sum_cards(p)
    # Check if player is on 21 or above
    if s_p == 21:
        if s_d == 21:
            if not suppress_print:
                print("Both have 21! Tied!")
                player1.budget += bet
            return ("Tie", "n")
        elif s_d != 21:
            if not suppress_print:
                print(f"{p.name} won with exact 21!")
                player1.budget += bet * 2
            return ("21", "p")
    elif s_d == 21:
        if not suppress_print:
            print(f"Dealer won with exact 21!")
        return ("21", "d")
    elif s_p > 21:
        if not suppress_print:
            print(f"{p.name} busted! Dealer won!")
        return ("Bust", "d")
    elif s_p == s_d:
        if not suppress_print:
            print(f"{p.name} won with exact 21!")
            player1.budget += bet
        return ("Tie", "n")
    elif s_p > s_d:
        if not suppress_print:
            print(f"{p.name} won with closer score!")
            player1.budget += bet * 2
        return ("Clean", "p")
    else:
        if not suppress_print:
            print("Dealer won with closer score!")
        return ("Clean", "d")

def sum_cards(subject):
    '''
    Sums players cards.
    '''
    s = 0
    for c in subject.all_cards:
        s += c.value
    return s

def more():
    '''
    Checks if player wants new game
    '''
    game = input("Do you want another game?(y/n): ")
    while game not in ["y","n"]:
        game = input("Please input valid value y or n: ")
    if game == "y":
        return True
    else:
        return False
    
# Start game loop
complete_game = True
while complete_game:
    game_alive = True
    player1 = Player(input("Enter your name: "))
    while game_alive:
        # Create new deck
        deck = Deck()
        deck.shuffle()
        # Deal first 2 cards to player and dealer
        dealer = Dealer()
        if player1.budget > 0:
            print(f"Your budget is: {player1.budget}")
            bet = int(input("Place your bet: "))
            while bet < 1 or player1.budget - bet < 0:
                bet = int(input("Enter valid number: "))
            player1.budget -= bet
            dealer.all_cards = []
            player1.all_cards = []
            for i in range(2):
                dealer.add_card(deck.deal_card())
                player1.add_card(deck.deal_card())
            # Check if anyone has 21 on start
            win = check_win(dealer, player1, True)
            if win[0] != "21":
                print(f"Summ of your cards is: {sum_cards(player1)}")
            else:
                check_win(dealer, player1, False)

        # Ask player if it wants to pull another one or is done
            player_pulling = True
            while player_pulling:
                pull_more = input("Do you want another card?(y/n): ")
                while pull_more not in ["y","n"]:
                    pull_more = input("Please input valid value y or n: ")
                if pull_more == "y":
                    player1.add_card(deck.deal_card())
                    win = check_win(dealer, player1, True)
                    print(f"Summ of your cards is: {sum_cards(player1)}")
                    if win[0] == "Bust":
                        win = check_win(dealer, player1, False)
                        if player1.budget > 0:
                            print(f"Your budget is: {player1.budget}")
                            game_alive = more()
                            break
                        else:
                            print("You lost all your money!")
                            break
                else:
                    player_pulling = False
                    win = check_win(dealer, player1, False)
                    if player1.budget > 0:
                        print(f"Your budget is: {player1.budget}")
                        game_alive = more()
                        break
        else:
            print("You lost all your money!")
            complete_game = more()
            break
    if not game_alive:
        complete_game = False
        print(f"You walked away with: {player1.budget}")
