# import
from ArrayStack import *
from ArrayQueue import *

def permutations(lst):
    # variables
    unused_items = ArrayStack()
    partial = ArrayQueue()
    perms = []

    # for-loop
    for index in range(len(lst)) :
        unused_items.push(lst[index]) # [1, 2, 3]
    
    # while-loop
    while not unused_items.is_empty(): 
        # variable
        missing = unused_items.pop() # 3, 2, 1

        # branching --> accoutn for liswt with one element
        if len(lst) == 1:
            perms.append(lst)
        else:
            for i in range(len(lst)):
                if lst[i] == missing:
                    # for-loop --> add partial permutations to the queue
                    for j in range(len(lst)): # 0, 1, 2
                        # branching --> determine what list segments to enqueue based on index
                        if lst[j] == missing:
                            if j == (len(lst) - 1):
                                partial.enqueue(lst[:i]) # [1, 2]
                                partial.enqueue(lst[::-1][1:]) # [2, 1]
                            elif j == 0:
                                partial.enqueue(lst[(i+1):])
                            else:
                                partial.enqueue(lst[:i] + lst[(i+1):])

        # while-loop --> place that missing item in each available
        while not partial.is_empty():
            # variable
            target = partial.dequeue() # [2, 3] (works), [1, 3] (works), [1, 2] (works) --> need [2, 1]
            
            # for-loop
            for item in lst: # 1, 2, 3
                # branching 
                if item not in target:
                    # for-loop --> put the missing value at each index of the list to create permutations
                    for index in range(len(lst) - 1): # 0, 1, 2
                        # adjust variables
                        new = target[:] # [1, 3] 
                        new.insert(index, item)
                            # [1, 2, 3], [2, 1, 3], [2, 3, 1] --> [2, 3]
                            # [2, 1, 3] (no), [1, 2, 3] (no), [1, 3, 2] --> [1, 3]
                            # [3, 1, 2], [1, 3, 2] (no), [1, 2, 3] (no) --> [1, 2]
                                # need [2, 1] for [3, 2, 1]
                        # branching --> do not allow repeats
                        if new not in perms:
                            perms.append(new)

    # return
    return perms
