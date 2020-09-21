"""
File: problem3_rearrange_digits.py
Author: Sidafa Conde
Email: sconde@umassd.edu
Github: sconde
Description: Rearrange Array Elements so as to form two number such that their sum is maximum.
"""


def partition(arr, low, high):
    pivot = arr[low]
    i, j = low, high

    while i < j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low] = arr[j]
    arr[j] = pivot

    # return the pivot index
    return j


def quick_sort_rec(arr, low, high):
    if high > low:
        pivot = partition(arr, low, high)
        quick_sort_rec(arr, low, pivot - 1)
        quick_sort_rec(arr, pivot + 1, high)


def quick_sort(arr):
    quick_sort_rec(arr, 0, len(arr) - 1)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return []

    # sort the list and reverse it
    quick_sort(input_list)
    input_list = input_list[::-1]

    x = 0
    for i in range(0, len(input_list), 2):
        x = x * 10 + input_list[i]

    y = 0
    for i in range(1, len(input_list), 2):
        y = y * 10 + input_list[i]

    return (x, y)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

# edge cases
test_function([[], []])
test_function([[1], [1]])
test_function([[1, 1, 1, 1, 1], [111, 11]])
