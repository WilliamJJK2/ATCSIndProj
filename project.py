#!/usr/bin/env python3

"""
deck.py
The deck for my BlackJack Game made for my Independent Project
"""

__author__ = "William Kim"
__version__ = "2024-05-17"

class Card():

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank
    
    def get_rank_value(self):
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        return ranks.index(self.rank) + 1
    
    def get_suit(self):
        return self.suit
    
    def __str__(self):
        return card.get_rank() + " of " + card.get_suit()
    
card = Card("Ace", "Spades")
print(card.get_rank())
print(card.get_rank_value())
print(card.get_suit())
print(card)


        