"""
lucky_triple.py

From Google foo.bar challenge:

A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With that information, you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

Write a function answer(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) where the list indices meet the requirement i < j < k.  The length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  The answer fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0. 

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the answer 3 total.

>>> answer([1, 1, 1])
1
>>> answer([1, 2, 4, 8])
4
>>> answer([1, 2, 4, 8, 1, 8, 9])
9
>>> answer([1, 2, 3, 4, 5, 6])
3
"""
from collections import defaultdict
from itertools import combinations

def answer(l):
    print(combination_lucky_triples(l))
    # return len(combination_lucky_triples(l))
    return dynamic_soln_lucky_triples(l)

def is_lucky_triple(triple):
    """ Returns x|y && y|z using modulo division
    """
    x, y, z = triple
    return not y%x and not z%y

def combination_lucky_triples(l):
    """ Returns set of lucky triples using itertools.combination to brute force check if every triple combination is a lucky triple. 
    Computes in O(n^3).
    """
    return set(triple for triple in combinations(l, 3)
                       if is_lucky_triple(triple))

def dynamic_soln_lucky_triples(l):
    """ Dynamic solution computes in O(n^2) time.
    """
    factors = defaultdict(lambda:[])
    triples = 0
    for x, y in combinations(l, 2):
        if not y%x:
            factors[y].append(x)
            triples += len(factors[x])
    return triples