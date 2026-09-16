"""
Problem 4a

input:
    values -- list of integers.
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Theta(n^2).
"""


def most_frequent_difference_a(values, d_mode) -> int:
    
    # 2 sum problem
    # double for loop
    # given the array and a target integer δmode, count how many ordered pairs (i, j) with i ≠ j satisfy ai − aj = δmode.
    
    counter = 0
    
    for i in range(len(values)):
        for j in range(len(values)):
            if(i != j):
                difference = values[i] - values[j]
                if (d_mode == difference):
                    counter = counter + 1
                    
    return counter