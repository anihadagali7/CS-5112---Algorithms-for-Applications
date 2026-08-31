def string_lengths(strings):
    """
    Return a dictionary mapping each string to its length.
    """
    
    print("printing the strings: ", strings)
    
    my_dict = {}
    
    for string in strings:
        length = len(string)
        
        my_dict[string] = length
        
    print("the dict now looks like: ", my_dict)
    
    return my_dict
