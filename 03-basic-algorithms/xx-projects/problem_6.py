"""
File: problem7_unsorted_integer_array.py
Author: Sidafa Conde
Email: sconde@umassd.edu
Github: sconde
Description: Max and Min in a Unsorted Array

In this problem, we will look for smallest and largest integer from a list of
unsorted integers. The code should run in O(n) time. Do not use Python's
inbuilt functions to find min and max.
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    n = len(ints)
    low, high = ints[0], ints[1]
    if low > high:
        high, low = low, high

    for i in range(2, n):
        if ints[i] > high:
            high = ints[i]
        elif ints[i] < low:
            low = ints[i]

    return (low, high)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
