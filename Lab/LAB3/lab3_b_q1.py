# Part B
def sorts_ints_and_floats(lst): # O(nlog(n)) --> merge sort (divide and conquer)
   # branching
    if len(lst) > 1: # base case
        # recursive variables
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        
        # recursion --> keeps dividing half into half until all elements are divided (divide)
        sorts_ints_and_floats(left)
        sorts_ints_and_floats(right)

        # variables
        index = ind = id = 0

        # while-loop
        while (index < len(left)) and (ind < len(right)):
            if type(left[index]) == type(right[ind]):
                if left[index] < right[ind]:
                    lst[id] = left[index]
                    index += 1

                else:
                    lst[id] = right[ind]
                    ind += 1

            else:
                if isinstance(type(left[index]), int):
                    lst[id] = left[index]
                    index += 1

                else:
                    lst[id] = right[ind]
                    ind += 1

            id += 1

        while index < len(left):
            lst[id] = left[index]
            index += 1
            id += 1
            
        while ind < len(right):
            lst[id] = right[ind]
            ind += 1
            id += 1
