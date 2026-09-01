from functools import reduce


def factorial_reduce(n):
    """
    Return n! using functools.reduce.
    """
    
    total = reduce(lambda x, y: x * y, range(1, n+1), 1)
    
    return total
