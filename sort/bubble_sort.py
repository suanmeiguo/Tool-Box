"""Bubble Sort Implementation"""
import copy


def sort(list_in):
    """Compare adjacent elements and move the small one to the left
    Recursive sort on the rest of the array
    """
    if type(list_in) != list:
        raise TypeError("Input must be a list")

    if len(list_in) == 0:
        return []

    result = copy.deepcopy(list_in)

    n = len(result)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]

    return result
