# Deck and card classes
from collections import namedtuple
import random

Card = namedtuple('Card', ['rank', 'suit'])

# class Card(object):
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit

#     def __repr__:
#         return f'Card(rank:{rank}, suit:{suit})'

class Deck(object):
    ranks = ['A'] + [str(n) for n in range(2,11)] + list('JQK')
    suits = ['clubs', 'diamonds', 'hearts', 'spades']

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        # self.cards = []
        # for suit in self.suits:
        #     for rank in self.ranks:
        #         self.cards.append(Card(rank, suit))

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):     
        return self._cards.pop() if len(self) else None
        # if (len(self)) > 0:
        #     return self._cards.pop()
        # else:
        #     return None
 
    def __repr__(self):
        output = ''
        for card in self._cards:
            output += str(card) + '\n'
        return output 

class FrenchDeck(Deck):
    def __init__(self):
        super(FrenchDeck, self).__init__()
        self.card_value = [Card(rank, suit) for rank in self.ranks
                                            for suit in self.suits]
        self._cards = self.card_value.copy()

    def deal(self):
        card = super(FrenchDeck, self).deal()
        return (card, self.card_value.index(card)+1)

if __name__ == '__main__':
    my_deck = Deck()
    # print(len(my_deck)) # return 52
    # print(my_deck[-1])
    # print(my_deck.deal())
    # print(my_deck[-1])
    # print(len(my_deck))
    my_deck.shuffle()
    print(my_deck)

    # french_deck = FrenchDeck()
    # for i in range(len(french_deck)):
    #     print(i, french_deck[i])
    # print(len(french_deck)) # return 52
    # print(french_deck[-1])
    # print(french_deck.deal())
    # print(french_deck[-1])
    # print(len(french_deck))    
    # french_deck.shuffle()
    # print(french_deck.deal())





