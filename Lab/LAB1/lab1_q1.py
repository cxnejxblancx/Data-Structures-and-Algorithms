def can_construct(word , letters):
    """
    word - type: str
    letters - type: str
    return value - type: bool
    """
    # variable
    word = [char for char in word] 

    # for-loop
    for letter in letters:
        if letter in word:
            word.remove(letter)
    
    # branch
    if len(word) == 0:
        return True
    else:
        return False
      
