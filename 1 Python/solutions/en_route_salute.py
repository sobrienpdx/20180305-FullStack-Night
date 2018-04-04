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

"""

def answer(s):
    left = []
    right = []
    count = 0
    for i in range(len(s)):
        if s[i] == '<':
            left.append((s[i], i))
        elif s[i] == '>':
            right.append((s[i], i))
    # print(left, right)
    for i in range(len(left)):
        for j in range(len(right)-1, -1, -1):
            l = left[i]
            r = right[j]
            # if l[1] >= r[1]:
            #     break
            # print(l, r)
            if l[1] - r[1] > 0:
                count += 1
    return count*2

