import random
import unittest

class Card:
    '''A class to create Cards'''
    def __init__(self, value, suit):
        '''intializes a card with a value and a suit'''
        self.value = value
        self.suit = suit
    def __repr__(self):
        '''returns a string displaying the value and suit of a card'''
        return f"Card({self.value} of {self.suit})"
    def __lt__(self, other):
        '''tests whether a card is of lower importance than another card'''
        if not isinstance(self, Card) or not isinstance(other, Card):
            raise TypeError(f"The arguments aren't both cards.") 
        elif self.suit != other.suit:
            return self.suit < other.suit
        else:
            return self.value < other.value
    def __eq__(self, other):
        '''tests whether two cards are the exact same'''
        if not isinstance(self, Card) or not isinstance(other, Card):
            raise TypeError(f"The arguments aren't both cards.")
        else:
            return (self.suit == other.suit and self.value == other.value)

class Deck:
    ''' Creates a deck of cards'''
    def __init__(self, values = range(1, 14), suits = ("clubs", "diamonds", "hearts", "suits")):
        '''intializes a deck of cards with cards of the values'''
        self.values = sorted(values)
        self.suits = sorted(suits)
        self.card_list = []
        for v in self.values:
            for s in self.suits:
                self.card_list.append(Card(v, s))
    def __len__(self): 
        '''returns the number of cards in the deck'''
        return len(self.card_list) 
    def sort(self):
        '''sorts the cards in the deck by the alphabetical order of the suit and the value of the card'''
        return self.card_list.sort()
    def __repr__(self):
        '''returns the cards in the deck and their values and suits'''
        return f"Deck: {self.card_list}"
    def shuffle(self):
        '''shuffles all the cards in the deck and puts them into a random order'''
        return random.shuffle(self.card_list)
    def draw_top(self):
        '''removes the last card in the deck and returns it'''
        if len(self.card_list) > 0:
            return self.card_list.pop(-1)
        else:
            raise RuntimeError ("There are no cards in the deck")

class Hand(Deck):
    ''' draws a hand of cards from the precreated deck'''
    def __init__(self, values, suits):
        '''intializes the hand of cards using the Deck initialization method'''
        Deck.__init__(self, values, suits)
    def __repr__(self):
        '''puts out the cards in the hand and their values and suits'''
        return f"Hand: {self.card_list}"
    def play(self):
        '''plays one of the cards in the hand'''
        if Card in card_list and len(self.card_list) > 0:
            return self.card_list.pop()
        elif len(self.card_list) <= 0:
            raise RuntimeError ("There are no cards in the hand")
        else:
            raise RuntimeError ("The requested cards aren't in the hand")



