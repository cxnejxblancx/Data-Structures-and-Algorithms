# a, b
def shift(lst, k, direction = "left"): # k < N
    # branching
    if direction == "left":
        # for-loop
        for iteration in range(k):
            # adjust variable
            lst.append(lst.pop(0))
    
    elif direction == "right":
        # for-loop
        for iteration in range(k):
            # adjust variable
            lst.insert(0, lst.pop()) 
