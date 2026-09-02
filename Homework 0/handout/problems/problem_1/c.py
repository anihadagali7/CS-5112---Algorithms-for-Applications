def process_numbers(numbers):
    """
    Print each positive number until a negative number is reached.

    Skip zeros using continue, and stop at the first negative number using
    break.
    """
    
    for num in numbers:
        if(num == 0):
            continue
        elif(num > 0):
            print(num)
        else:
            break
    
    pass
