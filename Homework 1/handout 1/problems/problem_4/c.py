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

    # subtract the current number from d_mode -> target
    # you now get the number you need from the rest of the list
    # pass that number into Counter, hoping to get count of target variable
    # add that to the counter

def most_frequent_difference_c(values, d_mode) -> int:
    
    counter = 0
    
    # create a hashmap of the values and frequency
    values_hash = {}
    
    for val in values:
        if(val in values_hash):
            values_hash[val] = values_hash[val] + 1
        else:
            values_hash[val] = 1
    
    for a in values:
        target = a - d_mode
        
        if(target in values_hash):
            # checking the same index, subtract one if same
            if(target == a):
                counter = counter + values_hash[target] - 1    
            else: 
                counter = counter + values_hash[target]
            
    return counter

# print("the answer is: ", most_frequent_difference_c([10, 9, 8, 3, 4, 5, 9, 11, 4, 6, 12], 6))
# print("the answer is: ", most_frequent_difference_c([5, 5, 5], 0))
# print("the answer is: ", most_frequent_difference_c([5, 5, 5], 0))
