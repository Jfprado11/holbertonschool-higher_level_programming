#!/usr/bin/python3
"""find the peak for a list """


def peak_binary(list_int, left, right, n):
    """find teh peak using a binary search"""
    mid = left + (right - left) / 2
    mid = int(mid)

    if ((mid == 0 or list_int[mid - 1] <= list_int[mid]) and
            (mid == n - 1 or list_int[mid + 1] <= list_int[mid])):
        return list_int[mid]
    elif mid > 0 and list_int[mid - 1] > list_int[mid]:
        return peak_binary(list_int, left, (mid - 1), n)
    else:
        return peak_binary(list_int, (mid + 1), right, n)


def find_peak(list_of_integers):
    """function to find a peak number"""
    n = len(list_of_integers)
    if n > 1:
        return(peak_binary(list_of_integers, 0, n - 1, n))
