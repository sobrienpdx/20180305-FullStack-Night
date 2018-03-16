# Solutions to practice03-lists
import random

"""Problem 1
Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.
"""
def random_element(a):
    return a[random.randint(0,len(a)-1)]

fruits = ['apples', 'bananas', 'pears']
random_element(fruits) # could return 'apples', 'bananas' or 'pears'

"""Problem 2
Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.
"""
def REPL_list():
    num_list = []
    while True:
        user_in = input("Enter a number (or 'done'): ").strip().lower()
        try:
            num_list.append(int(user_in))
        except:
            if user_in == 'done':
                break
    print(num_list)

REPL_list()
# Enter a number (or 'done'): 5
# Enter a number (or 'done'): 34
# Enter a number (or 'done'): 515
# Enter a number (or 'done'): done
# [5, 34, 515]

"""Problem 3
Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.
"""
def eveneven(nums):
    pass

eveneven([5, 6, 2]) # → True
eveneven([5, 5, 2]) # → False

"""Problem 4
Print out every other element of a list, first using a while loop, then using a for loop.
"""
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print_every_other(nums) # → 0, 2, 4, 6, 8

"""Problem 5
Write a function that returns the reverse of a list.
"""
def reverse(nums):
    pass

"""Problem 6
Write a function to move all the elements of a list with value less than 10 to a new list and return it.
"""
def extract_less_than_ten(nums):
    pass

"""Problem 7
Write a function to find all common elements between two lists.
"""
def common_elements(nums1, nums2):
    pass

"""Problem 8
Write a function to combine two lists of equal length into one, alternating elements.
"""
def combine(nums1, nums2):
    pass

combine(['a','b','c'],[1,2,3]) # → ['a', 1, 'b', 2, 'c', 3]

"""Problem 9
Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number
"""
def find_pair(nums, target):
    pass

nums = [5, 6, 2, 3]
target = 7
find_pair(nums, target) # → [5, 2]
# Optional: return a list of all pairs of numbers that sum to a target value.


"""Problem 10
Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.
"""
def merge(list1, list2):
    pass

merge([5,2,1], [6,8,2]) # → [[5,6],[2,8],[1,2]]

"""Problem 11
Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.
"""
def combine_all(list_of_lists):
    pass

nums = [[5,2,3],[4,5,1],[7,6,3]]
combine_all(nums) # → [5,2,3,4,5,1,7,6,3]

"""Problem 12
Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.
"""
def fibonacci(n):
    pass

fibonacci(8) # → [1, 1, 2, 3, 5, 8, 13, 21]

"""Problem 13
Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.
"""
def minimum(nums):
    pass

def maxmimum(nums):
    pass

def mean(nums):
    pass

def mode(nums): # (OPTIONAL)
    pass

"""Problem 14
Write a function which takes a list as a parameter and returns a new list with any duplicates removed.
"""
def find_unique(nums):
    pass

nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique_nums = find_unique(nums) # → [12, 24, 35, 88, 120, 155]