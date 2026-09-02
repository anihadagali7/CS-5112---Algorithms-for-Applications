def pop_element_at(lst, index):
    """
    Pop and return the element at index, or return None for an invalid index.
    """
    
    if(index < 0 or index >= len(lst)):
        return 'None'
    else:
        return lst.pop(index)
