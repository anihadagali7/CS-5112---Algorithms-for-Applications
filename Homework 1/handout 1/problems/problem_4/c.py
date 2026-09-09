"""
Problem 4c

input:
    values -- list of integers.
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Theta(n).
"""

from collections import Counter
import copy


def most_frequent_difference_c(values, d_mode) -> int:
    
    # subtract the current number from d_mode -> target
    # you now get the number you need from the rest of the list
    # pass that number into Counter, hoping to get count of target variable
    # add that to the counter
    
    counter = 0
    
    for n in range(len(values)):
        target = values[n] - d_mode
        
        deep_copy = copy.deepcopy(values)
        deep_copy.pop(n)
        counts = Counter(deep_copy)
        
        counts_target = list(counts.elements()).count(target)
        
        counter = counter + counts_target
        
    return counter
