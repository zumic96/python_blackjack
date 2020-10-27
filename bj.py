'''
Milestone Project 2 - BlackJack
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10}

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        if rank == 'Ace':
            self.value = 0
        else:
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

# Create new deck
deck = Deck()
# Deal first 2 cards to player and dealer
dealer = Dealer()
player1 = Player("player1")
for i in range(2):
    dealer.add_card(deck.deal_card())
    player1.add_card(deck.deal_card())
# Check if anyone has 21

# Ask player if it wants to pull another one or is done
