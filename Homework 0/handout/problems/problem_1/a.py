def categorize_number(n):
    """
    Categorize n as "negative", "zero", or "positive".
    """
    
    if(n < 0):
        return "negative"
    elif(n > 0):
        return "positive"
    else:
        return "zero"
