"""
Problem 4b

input:
    values -- list of integers.
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Theta(n log n).
"""

from bisect import bisect_left, bisect_right
from collections import Counter


def most_frequent_difference_b(values, d_mode) -> int:
    # sort the list
    # iterate through the list, find the target
    # check which side of the list we should go to
    # get first occurrence of the target with bisect_left
    # get last occurrence of the target with bisect_right
    
    values.sort()
    
    counter = 0
    
    for index, val in enumerate(values):
        target = val - d_mode
        frequency = 0
        
        index_left = bisect_left(values, target)
        index_right = bisect_right(values, target)
        
        frequency = index_right - index_left
        if(target == val):
            frequency = frequency - 1
        
        counter = counter + frequency
        
    return counter
