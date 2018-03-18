# Deck and card classes
from collections import namedtuple
import random

Card = namedtuple('Card', ['rank', 'suit'])

class Deck(object):
    ranks = ['A'] + [str(n) for n in range(2,11)] + list('JQK')
    suits = ['clubs', 'diamonds', 'hearts', 'spades']

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):     
        return self._cards.pop() if len(self) else None