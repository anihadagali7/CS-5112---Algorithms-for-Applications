"""
Problem 1a

input: List of integers.
output: Maximum sum of non-adjacent elements.

TODO: implement your solution.
"""


def maxsum_list(xs) -> int:
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