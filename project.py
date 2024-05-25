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
        if self.rank == "Jack" or "Queen" or "King":
            return 10
        elif self.rank == "Ace":
            return 11
        else:
            return int(self.rank)
    
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
        print("Deck shuffled.")

    def draw_card(self):
        if not self.cards:
            print("The deck is empty.")
            return None
        return self.cards.pop(0)

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.get_rank_value()
        if card.get_rank() == "Ace":
            self.aces += 1
        self.ace_value()

    def ace_value(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
    def display_hand(self):
        return "value: " + str(self.value)

def hit(deck, hand):
    hand.add_card(deck.draw_card())

def is_busted(hand):
    return hand.value > 21
    
def compare_hands(player_hand, dealer_hand):
    if player_hand.value > dealer_hand.value:
        return "Player wins!"
    elif player_hand.value < dealer_hand.value:
        return "Dealer wins!"
    else:
        return "Tie!"

def main():
    print("Welcome to BlackJack!")
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    i = 0
    while i <= 1:
        player_hand.add_card(deck.draw_card())
        dealer_hand.add_card(deck.draw_card())
        i += 1
    
    while True:
        action = input("Would you like to hit or stand? (h/s): ").lower()
        if action == "h":
            hit(deck, player_hand)
            print(player_hand.display_hand())
            if is_busted(player_hand):
                print("Player busts! Dealer wins.")
                return
        elif action == "s":
            break
        else:
            print("Invalid input, Please enter 'h' or 's'.")

        
    while dealer_hand.value < 17:
        hit(deck, dealer_hand)
        print(dealer_hand.display_hand())

    if is_busted(dealer_hand):
        print("Dealer busts! Player wins.")
    else:
        print(dealer_hand.display_hand())
        result = compare_hands(player_hand, dealer_hand)
        print(result)
            

if __name__ == "__main__":
    main()