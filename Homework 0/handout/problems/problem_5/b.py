def factorial_rec(n):
    """
    Return n! using recursion.
    """
    
    if(n <= 1):
        return 1
    else:
        return n * factorial_rec(n-1)
