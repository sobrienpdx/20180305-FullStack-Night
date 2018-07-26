# Fibonacci.py with caching
import time, json, os


def calc_time(fn):
    """ Calculates execution time of function f
    """
    def timed(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        print(f"Completed in {time.time()-start} seconds.")
        return result
    return timed

def memoize(fn):
    """ Memoization decorator to give fibonacci() equivalent optimization as optimized_fibonacci()
    """
    memo = {}
    def call(n):
        if n not in memo:
            memo[n] = fn(n)
        return memo[n]
    return call

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

@memoize
def fibonacci(n):
    """
    Finds nth fibonacci without caching
    """
    if 0<=n<2: # base case
        return 1
    return fibonacci(n-1) + fibonacci(n-2) # recursive case

if __name__ == '__main__':
    n = int(input("How many fibonacci numbers do you want to calculate: ").strip().replace(',',''))
    # print(f"In optimized_fibonacci(): Calculating first {n} fibonacci numbers")
    # start_time = time.time()
    # for i in range(n+1):
    #     fibonacci(i)
    # print(f"The {n}th fibonacci number is {optimized_fibonacci(n)}")
    # print(f"Completed in {time.time()-start_time} seconds")
    print(f"In fibonacci() with memoization:")
    start_time = time.time()
    print(f"The {n}th fibonacci number is {fibonacci(n)}")
    print(f"Completed in {time.time()-start_time} seconds")


