"""
File: square_root_integer.py
Author: Sidafa Conde
Email: sconde@umassd.edu
Github: sconde
Description: Calculate the floored square root of a number
"""


def sqrt(number):
    """
    Calculate the floored square root of a number using bisection root finding algorithm

    solving y = x^2 - S
    Time complexity: O( log n ) - where n -

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if not isinstance(number, int):
        print('Invalid input')
    elif number in (0, 1):
        return number

    start, end, mid = 1, number, number

    while start < end:
        mid = (start + end) // 2
        mid_square = mid * mid

        if mid_square == number:
            return mid
        elif mid_square < number:
            start = mid + 1
        else:
            end = mid - 1

    return mid


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
