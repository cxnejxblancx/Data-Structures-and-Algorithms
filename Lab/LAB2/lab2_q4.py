# b
def vc_count(word, low, high): 
    """
    : word type: str
    : low, high type: int
    : return type: tuple (int, int)
    """
    # branching
    if low >= high:
        if word[low] in "aeiouAEIOU":
            return (1, 0)
        
        else:
            return (0, 1)
    else:
        other = vc_count(word, (low + 1), high)

        if word[low] in "aeiouAEIOU":
            return (other[0] + 1, other[1])
        
        else:
            return (other[0], other[1] + 1)
          
