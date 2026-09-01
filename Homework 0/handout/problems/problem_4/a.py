def square_all(numbers):
    """
    Return a list of squares of all numbers.
    """
    
    answer = []
    
    for num in numbers:
        square = num * num
        
        answer.append(square)
    
    return answer


def filter_even(numbers):
    """
    Return only the even numbers from numbers.
    """
    
    def even(n):
        return n % 2 == 0;
    
    answer = list(filter(even, numbers))
    
    return answer
