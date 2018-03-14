# Solutions to practice01-fundamentals

"""
Problem 1: 
Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)
"""
def is_even(a):
	return a%2 == 0 

is_even(5) # → False
is_even(6) # → True

"""
Problem 2:
Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.
"""
def opposite(a, b):
	return (a>0 and b<0) or (a<0 and b>0)

opposite(10, -1) # → True
opposite(2, 3) # → False
opposite(-1, -1) # → False

"""
Problem 3:
Write a function that returns True if a number within 10 of 100.
"""
def near_100(num):
    pass

near_100(50) # → False
near_100(99) # → True
near_100(105) # → True

"""
Problem 4:
Write a function that returns the maximum of 3 parameters.
"""
def maximum_of_three(a, b, c):
    pass

maximum_of_three(5,6,2) # → 6
maximum_of_three(-4,3,10) # → 10

"""
Problem 5
Print out the powers of 2 from 2^0 to 2^20
"""
def powers_of_2(n):
	pass

print(powers_of_2(20)) # → 1, 2, 4, 8, 16, 32, ..., 1048576
