# Runtime = O(n)
def split_parity(lst):
    # variable --> Pointer (Runtime = O(1))
    start = 0

    # for-loop --> Swap even with the first next odd (Runtime = O(n))
    for index in range(len(lst)):
        if lst[index] % 2 != 0:
            # adjust variables
            lst[start], lst[index] = lst[index], lst[start] # Swap even number with next odd number
            start += 1 # Adjust tracker of last even number

    # return
    return lst
