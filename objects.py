
# objects.py
# Core game objects for Blackjack: Card, Deck, Hand

import random

# Constants
SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11  # Default Ace to 11
}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        return VALUES[self.rank]

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def dealCard(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def getTotal(self):
        total = 0
        aces = 0
        for card in self.cards:
            val = card.value()
            total += val
            if card.rank == 'Ace':
                aces += 1
        # Adjust Aces from 11 to 1 as needed
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def isBust(self):
        return self.getTotal() > 21

    def isBlackjack(self):
        return self.getTotal() == 21

    def shortDisplay(self):
        return ' '.join(str(card) for card in self.cards)
