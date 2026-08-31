def even_values_keys(data):
    """
    Return the keys whose values are even numbers.
    """
    
    answer = []
    
    for key in data:
        if(key % 2 == 0):
            answer.append(key)
            
    return answer


def square_evens(numbers):
    """
    Return a list of squares of the even numbers in numbers.
    """
    
    answer = []
    
    for num in numbers:
        if(num % 2 == 0):
            square = num * num
            answer.append(square)
        
    return answer


def long_strings(strings):
    """
    Return all strings with length greater than 5.
    """
    
    answer = []
    
    for str in strings:
        if(len(str) > 5):
            answer.append(str)
            
    return answer


def convert_to_celsius(fahrenheit_temps):
    """
    Convert Fahrenheit temperatures to Celsius strings.

    Append " Freezing" when the original Fahrenheit temperature is at or below
    32.
    """
    pass
