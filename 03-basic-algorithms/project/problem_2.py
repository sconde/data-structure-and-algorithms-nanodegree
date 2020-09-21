"""
File: rotated_array_search.py
Author: Sidafa Conde
Email: sconde@umassd.edu
Github: sconde
Description: find index in a rotated sorted array
"""


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Using binary search

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    start, end = 0, len(input_list) - 1
    if start > end:
        return -1

    while start <= end:
        mid = start + (end - start)//2

        if input_list[mid] == number:
            return mid

        if input_list[start] <= input_list[mid] and input_list[mid] >= number >= input_list[start]:
            end = mid - 1

        elif input_list[mid] <= input_list[end] and input_list[mid] <= number <= input_list[end]:
            start = mid + 1

        elif input_list[start] <= input_list[mid] <= input_list[end] < number:
            start = mid + 1

        elif input_list[end] <= input_list[mid]:
            start = mid + 1

        elif input_list[start] >= input_list[mid]:
            end = mid - 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# edge case
test_function([[], 10])
test_function([[1], 1])
test_function([[1], 0])
test_function([list(range(0, 15)), 5])
