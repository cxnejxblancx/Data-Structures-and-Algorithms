# a
def reverse_list(lst):
    """
    : lst type: list[]
    : return type: None 
    """
    # for-loop
    for element in range(len(lst) // 2):
        # adjust variable
        lst[element], lst[-(element + 1)] = lst[-(element + 1)], lst[element]

# b
def sum_to(n):
    """
    : n type: int
    : return type: int
    """
    # branching
    if n == 1: # base case
        return 1
    
    else: # recursive case
        return n + sum_to(n-1)
    
