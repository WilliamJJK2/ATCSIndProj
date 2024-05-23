#!/usr/bin/env python3

"""
project.py
The BlackJack Game made for my Independent Project
"""

__author__ = "William Kim"
__version__ = "2024-05-17"

import random

class Card():

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank
    
    def get_rank_value(self):
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        if ranks[ranks.index(self.rank)] == "Jack" or "Queen" or "King":
            return 10
        elif ranks[self.rank] == "Ace":
            return 11
        else:
            return ranks.index(self.rank) + 1
    
    def get_suit(self):
        return self.suit
    

class Deck():

    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            print("The deck is empty.")
            return None
        return self.cards.pop(0)

def main():
    card = Card("Ace", "Spades")
    print(card.get_rank())
    print(card.get_rank_value())
    print(card.get_suit())
    print(card.get_rank() + " of " + card.get_suit())

if __name__ == "__main__":
    main()