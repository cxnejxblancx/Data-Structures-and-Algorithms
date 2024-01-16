# Runtime = O(log(n))
def findChange(lst01):
    # variables --> (Runtime = O(1))
    low = 0
    high = len(lst01) - 1

    # flag --> (runtime = O(1))
    found = False

    # while-loop --> (Runtime = O(log(n)))
    while (low <= high) and (found == False):
        # variable
        mid = (low + high) // 2

        # branching
        if lst01[mid] == 0:
            # adjust variable
            low = mid + 1

        else:
            if lst01[mid - 1] == 0:
                # adjust flag
                found = True

                # return
                return mid
            
            else: 
                # adjust variables
                high = mid - 1

    # branching --> (Runtime = O(1))
    if found == False:
        return None
