
# Name: Meron Assefa
# Class: DEV 128
# Date: [June,20,2024]
# Description: Phase 3 of Blackjack Game – contains the business logic (Blackjack class) 
# that handles player and dealer turns, determines game outcomes, and manages money.


import random
from objects import Deck, Hand

class Blackjack:
    def __init__(self, starting_money):
           # Initialize game money, deck, and empty hands
        self.money = starting_money
        self.bet = 0
        self.deck = Deck()
        self.playerHand = Hand()
        self.dealerHand = Hand()

    def setupRound(self):
        # Create and shuffle a new deck
        self.deck.shuffle()
        # Start with new empty hands
        self.playerHand = Hand()
        self.dealerHand = Hand()
        self.playerHand.addCard(self.deck.dealCard())
        self.playerHand.addCard(self.deck.dealCard())
        self.dealerHand.addCard(self.deck.dealCard())

    def takePlayerTurn(self):
         # Deal one more card to the player's hand
        self.playerHand.addCard(self.deck.dealCard())

    def takeDealerTurn(self):
                # Dealer draws second card

        self.dealerHand.addCard(self.deck.dealCard())
        while self.dealerHand.getTotal() < 17:
            self.dealerHand.addCard(self.deck.dealCard())

    def determineOutcome(self):
        player_total = self.playerHand.getTotal()
        dealer_total = self.dealerHand.getTotal()
                # Player busts

        if self.playerHand.isBust():
            self.money -= self.bet
            return "Sorry. You busted. You lose."
         # Dealer busts
        if self.dealerHand.isBust():
            self.money += self.bet
            return "Yay! The dealer busted. You win!"
           # Blackjack win
        if self.playerHand.isBlackjack() and len(self.playerHand.cards) == 2:
            self.money += int(1.5 * self.bet)
            return "Blackjack! You win!"
        # Compare totals

        if player_total > dealer_total:
            self.money += self.bet
            return "Hooray! You win!"
        elif player_total < dealer_total:
            self.money -= self.bet
            return "Sorry. Dealer wins."
        else:
            return "You push."
