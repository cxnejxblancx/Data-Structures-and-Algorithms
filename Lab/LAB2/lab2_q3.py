# a
def binary_search_lowercase(lst, char):
    """
    : lst type: list[str]
    : char type: str
    : return type: int
    """
    # variables
    left = 0
    right = len(lst) - 1
    index = -1
    found = False

    # while-loop
    while (found == False) and (left <= right):
        # variable
        mid = (left + right) // 2

        # branching
        if lst[mid] == char:
            # adjust variables
            found = True
            index = mid
        
        elif lst[mid] < char:
            # adjust variable
            right = mid - 1

        else:
            # adjust variable
            left = mid + 1

    # return
    return index

# b
    # a) runtime = O(n^2) --> slices a list and creates a new one each time

    # b)
def find_max(lst, low, high):
    """
    : lst type: list[int]
    : low, high type: int
    : return type: int
    """
    # branching
    if low == high: # base case
        # return
        return lst[low]

    # variable --> Pointer
    max = find_max(lst, (low + 1), high)

    # branching 
    if lst[low] > max:
        max = lst[low]

    # return
    return max
