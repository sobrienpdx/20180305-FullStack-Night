"""
en_route_salute.py

From Google foo.bar challenge:
Write a program that counts how many salutes are exchanged during a typical walk along a hallway. The hall is represented by a string. For example:
"--->-><-><-->-"

Each hallway string will contain three different types of characters: '>', an employee walking to the right; '<', an employee walking to the left; and '-', an empty space. Every employee walks at the same speed either to right or to the left, according to their direction. Whenever two employees cross, each of them salutes the other. They then continue walking until they reach the end, finally leaving the hallway. In the above example, they salute 10 times.

Write a function which takes a string representing employees walking along a hallway and returns the number of times the employees will salute. The input string will contain at least 1 and at most 100 characters, each one of -, >, or <.

DOCTESTS:
>>> answer(">----<")
2
>>> answer("<<>><")
4
>>> answer("<<->->-<")
4
>>> answer("<->")
0
>>> answer("<>->")
0
>>> answer(">--------------------------------------------------------------------------------------------------------------------------------<<")
4
>>> answer("<<>><<<>><")
20
>>> answer("<<>><<<>><<<>><<<>><")
88
"""
import time

def print_runtime(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__}({args}, {kwargs}) completed in {end_time-start_time} seconds")
        return result

    wrapper.__name__ = func.__name__
    return wrapper    


def answer(s):
    return calc_salutes_in_linear_time(s)


def calc_salutes_in_linear_time(s):
    """ Optimized solution with O(n) = n
    """
    salutes = 0
    lefts = 0
    for i in range(len(s)):
        if s[i] == '>':
            lefts += 1
        elif s[i] == '<':
            salutes += lefts 
    return salutes*2
    

def calc_salutes_in_n_squared_time(s):  
    """ First solution with O(n) = n^2 (triangular sequence)
    """
    salutes = 0
    for i in range(len(s)):
        if s[i] == '>':
            for j in range(len(s)-1, -1, -1):
                if i >= j:
                    break
                if s[j] == '<':
                    salutes += 1
    return salutes*2    