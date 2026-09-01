from functools import reduce


def product_of_all(numbers):
    """
    Return the product of all numbers in numbers using reduce.
    """
    
    total = reduce(lambda x,y: x*y, numbers)
    
    return total
