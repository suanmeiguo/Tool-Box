"""Insertion Sort Implementation"""
import copy


def sort(list_in):
    """Create a new space and add each element in sorted order to the new space
    """
    if type(list_in) != list:
        raise TypeError("Input must be a list")

    if len(list_in) == 0:
        return []

    result = []

    for e in list_in:
        n = len(result)
        if n == 0:
            result.append(e)
            continue

        # start comparing from beginning of new list
        insertion_flag = False
        for i in range(n):
            if e < result[i]:
                insertion_flag = True
                break

        if insertion_flag:
            # expand space
            result.append(result[n - 1])

            # shift
            for j in range(n - 1, i, -1):
                result[j] = result[j - 1]
            result[i] = e
        else:
            result.append(e)

    return result
