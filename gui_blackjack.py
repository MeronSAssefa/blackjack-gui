
# Name: Meron Assefa
# Class: DEV 128
# Date: [June,20,2024]
# Description: Phase 3 of Blackjack Game – GUI built with tkinter to allow users to play 
# a simplified version of Blackjack. Implements all necessary event handlers and user interaction logic.


import tkinter as tk
from tkinter import ttk
from blackjack import Blackjack
from objects import Card, Hand, Deck

STARTING_BALANCE = 100

class BlackjackFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
         # GUI state variables (linked to entry fields)
        self.money = tk.StringVar()
        self.bet = tk.StringVar()
        self.dealerCards = tk.StringVar()
        self.dealerPoints = tk.StringVar()
        self.playerCards = tk.StringVar()
        self.playerPoints = tk.StringVar()
        self.result = tk.StringVar()
        # Create a Blackjack game instance and set game status
        self.game = Blackjack(STARTING_BALANCE)
        self.gameOver = True
        # Set up GUI layout
        self.initComponents()
        self.money.set("$" + str(self.game.money))
        self.bet.set("0")

    def initComponents(self):
        self.pack()
                # Labels and entry fields for money and bet

        ttk.Label(self, text="Money:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.money, state="readonly").grid(column=1, row=0, sticky=tk.W)
        ttk.Label(self, text="Bet:").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.bet).grid(column=1, row=1, sticky=tk.W)
        ttk.Label(self, text="DEALER").grid(column=0, row=2, sticky=tk.E)
        ttk.Label(self, text="Cards:").grid(column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=50, textvariable=self.dealerCards, state="readonly").grid(column=1, row=3, sticky=tk.W)
        ttk.Label(self, text="Points:").grid(column=0, row=4, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.dealerPoints, state="readonly").grid(column=1, row=4, sticky=tk.W)
        ttk.Label(self, text="YOU").grid(column=0, row=5, sticky=tk.E)
        ttk.Label(self, text="Cards:").grid(column=0, row=6, sticky=tk.E)
        ttk.Entry(self, width=50, textvariable=self.playerCards, state="readonly").grid(column=1, row=6, sticky=tk.W)
        ttk.Label(self, text="Points:").grid(column=0, row=7, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.playerPoints, state="readonly").grid(column=1, row=7, sticky=tk.W)
        self.makeButtons1()
        ttk.Label(self, text="RESULT:").grid(column=0, row=9, sticky=tk.E)
        ttk.Entry(self, width=50, textvariable=self.result, state="readonly").grid(column=1, row=9, sticky=tk.W)
        self.makeButtons2()
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons1(self):
        buttonFrame = ttk.Frame(self)
        buttonFrame.grid(column=1, row=8, sticky=tk.W)
        ttk.Button(buttonFrame, text="Hit", command=self.hit).grid(column=0, row=0)
        ttk.Button(buttonFrame, text="Stand", command=self.stand).grid(column=1, row=0)

    def makeButtons2(self):
        buttonFrame = ttk.Frame(self)
        buttonFrame.grid(column=1, row=10, sticky=tk.W)
        ttk.Button(buttonFrame, text="Play", command=self.play).grid(column=0, row=0)
        ttk.Button(buttonFrame, text="Exit", command=self.exit).grid(column=1, row=0)

    def displayPlayer(self):
        self.playerCards.set(self.game.playerHand.shortDisplay())
        self.playerPoints.set(str(self.game.playerHand.getTotal()))

    def displayDealer(self):
        self.dealerCards.set(self.game.dealerHand.shortDisplay())
        self.dealerPoints.set(str(self.game.dealerHand.getTotal()))

    def displayResult(self):
        self.result.set(self.game.determineOutcome())
        self.money.set(f"${self.game.money}")

    def playerCanPlayTurn(self):
        if self.gameOver:
            self.result.set("Please click Play to start a game.")
            return False
        self.result.set("")
        return True

    def hit(self):
        if not self.playerCanPlayTurn():
            return
        self.game.takePlayerTurn()
        self.displayPlayer()
        if self.game.playerHand.isBust():
            self.gameOver = True
            self.displayResult()

    def stand(self):
        if not self.playerCanPlayTurn():
            return
        self.gameOver = True
        self.game.takeDealerTurn()
        self.displayDealer()
        self.displayResult()

    def play(self):
        if not self.gameOver:
            self.result.set("Game already in progress. Click Hit or Stand.")
            return
        try:
            bet = int(self.bet.get())
        except ValueError:
            self.result.set("Invalid bet amount.")
            return
        if bet <= 0 or bet > self.game.money:
            self.result.set("Bet must be positive and within your balance.")
            return

        self.gameOver = False
        self.game.bet = bet
        self.game.setupRound()
        self.displayPlayer()
        self.displayDealer()
        # Check for immediate blackjack
        if self.game.playerHand.isBlackjack():
            self.gameOver = True
            self.displayResult()

    def exit(self):
        self.parent.destroy()
 # Start the game window
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Blackjack")
    BlackjackFrame(root)
    root.mainloop()
