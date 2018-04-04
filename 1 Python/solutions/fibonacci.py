# Fibonacci.py with caching
import time, json, os

cached_fibonacci = {0:1, 1:1} # base cases 

def optimized_fibonacci(n):
    """
    Finds nth fibonacci using caching
    """
    if n in cached_fibonacci.keys(): # checks if n is in our stored fibonacci numbers
        return cached_fibonacci[n]
    else: # calculates and adds the nth fibonacci number to our cache
        cached_fibonacci[n] = optimized_fibonacci(n-1) + optimized_fibonacci(n-2) 
        return cached_fibonacci[n]


def fibonacci(n):
    """
    Finds nth fibonacci without caching
    """
    if 0<=n<2: # base case
        return 1
    return fibonacci(n-1) + fibonacci(n-2) # recursive case


if __name__ == '__main__':

    start_time = time.time()
    n = int(input("How many fibonacci numbers do you want to calculate: ").strip().replace(',',''))
    print(f"Calculating first {n} fibonacci numbers")
    start_time = time.time()
    for i in range(n+1):
        optimized_fibonacci(i)
    print(f"Completed in {time.time()-start_time} seconds")
    print(f"The {n}th fibonacci number is {optimized_fibonacci(n)}")
