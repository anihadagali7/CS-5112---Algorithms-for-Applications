def get_keys(data):
    """
    Return a list of all keys in data.
    """
    
    answer = []
    
    for key, value in data.items():
        answer.append(key)
        
    return answer


def get_values(data):
    """
    Return a list of all values in data.
    """
    answer = []
    
    for key, value in data.items():
        answer.append(value)
        
    return answer


def get_items(data):
    """
    Return a list of all key-value pairs in data.
    """
    
    list(data.items())
    
    pass


def get_value(data, key, default=None):
    """
    Return data[key] when present, otherwise return default.
    """
    
    return data.get(key, default)
