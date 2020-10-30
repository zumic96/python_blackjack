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
    def __init__(self,name):
        self.all_cards = []
        self.name = name
    def add_card(self,card):
        self.all_cards.append(card)

def check_win(d, p, suppress_print):
    '''
    Check who won, player or dealer.
    '''
    s_d = sum_cards(d)
    s_p = sum_cards(p)
    # Check if player is on 21 or above
    if s_p == 21:
        if s_d == 21:
            print("Both have 21! Tied!")
            return ("Tie", "n")
        elif s_d != 21:
            print(f"{p.name} won with exact 21!")
            return ("21", "p")
    elif s_d == 21:
        print(f"Dealer won with exact 21!")
        return ("21", "d")
    elif s_p > 21:
        print(f"{p.name} busted! Dealer won!")
        return ("Bust", "d")
    elif s_p == s_d:
        print(f"{p.name} won with exact 21!")
        return ("Tie", "n")
    elif s_p > s_d:
        print(f"{p.name} won with closer score!")
        return ("Clean", "p")
    else:
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
    
# Start game loop
game_alive = True
while game_alive:
    # Create new deck
    deck = Deck()
    # Deal first 2 cards to player and dealer
    dealer = Dealer()
    player1 = Player(input("Enter your name: "))
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
    pull = input("Do you want another card?(y/n): ")
    while pull not in ["y","n"]:
        pull = input("Please input valid value y or n: ")
    if pull == "y":
        player1.add_card(deck.deal_card())
        print(f"Summ of your cards is: {sum_cards(player1)}")
    else:
        win = check_win(dealer, player1, False)
        game_alive = input("Do you want another game?(y/n): ")
        while game_alive not in ["y","n"]:
            game_alive = input("Please input valid value y or n: ")
        if game_alive == "y":
            game_alive = True
        else:
            game_alice = False
