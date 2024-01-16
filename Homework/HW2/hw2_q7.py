def split_by_sign(lst, low, high):
    # branching
    if low > high: # base case
        return
    
    else: # recusive cases
        # branching
        if lst[low] > 0: # If lst[low] is positive, make the following adjustments...
            # branching
            if lst[high] < 0: # If lst[high] is negative, switch lst[low] and lst[high] so they are in the correct positions --> evaluate the lst from the the next index
                # adjust variables
                lst[low], lst[high] = lst[high], lst[low]
                split_by_sign(lst, (low + 1), high)
                
            else: # Otherwise, lst[high] is in the right place --> evaluate lst from the same index to one less than the last index
                split_by_sign(lst, low, (high - 1))

        else: #Otherwise, it is in the correct spot --> evaluate lst starting at the next index
            split_by_sign(lst, (low + 1), high)

    # return
    return lst
