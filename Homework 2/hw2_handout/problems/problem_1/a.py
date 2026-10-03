"""
Problem 1a

input: List of integers.
output: Maximum sum of non-adjacent elements.

TODO: implement your solution.
"""


def maxsum_list(xs) -> int:
    
    # brute force is 
    # keep track of indices that you use
    # keep track of sum
    # maybe keep an array of all elements, and turn them to true/false if used
    
    # dynamic programming
    # i need to divide into smaller sub problems
    # keep splicing the array
    # compare two numbers, return the larger of the two, since they are adjacent
    
    # [3, 4, 5, 8, 9, 1, 2] -> start
    # [3, 4, 5, 8, 9, 10, 2]
    # [3, 4, 5, 8, 9, 1, 2]
    # [3, 4, 5, 8, 9, 1, 2]
    
    # start at the back
    # at each number, i choose between keeping it or not keeping it
    # if i keep it, i need to skip the next number. add number to running total if i keep it
    n = len(xs)
    
    memo = [None] * (n + 1)
    
    return recursive_helper(xs, n, memo)

def recursive_helper(list, n, memo):
    # base case
    if(n == 0):
        return 0
    
    if(n == 1):
        return list[0]
    
    if(memo[n] != None):
        return memo[n]
    
    pick = list[n - 1] + recursive_helper(list, n - 2, memo)
    notPick = recursive_helper(list, n - 1, memo)
    
    memo[n] = max(pick, notPick)

    return memo[n]


print("max sum list: ", maxsum_list([3, 4, 5, 8, 9, 1, 2]))