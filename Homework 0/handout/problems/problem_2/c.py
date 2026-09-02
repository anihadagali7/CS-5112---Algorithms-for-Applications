def remove_element(lst, element):
    """
    Remove the first occurrence of element from lst, if present.
    """
    
    for (index, val) in enumerate(lst):
        if(val == element):
            lst.pop(index)
            return lst
        
    return lst
