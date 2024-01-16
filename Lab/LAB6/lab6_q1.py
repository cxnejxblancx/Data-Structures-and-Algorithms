# import
from Lab6 import *

# a
def invert_bt(root):
    '''
    Inverts the binary tree using recursion
    '''
    # branching
    if (root == None):
        return
    
    # variables --> recursion
    left = invert_bt(root.left)
    right = invert_bt(root.right)
    
    # adjust variables
    root.left = right
    root.right = left

    # return
    return root

# b
def most_frequent(lst):
    # variable
    fmap = {}

    # for-loop
    for num in lst: 
        # branching
        if num not in fmap:
            fmap[num] = 0
        fmap[num] += 1
    
    # variables
    max_num = None
    max_count = 0

    # for-loop
    for key in fmap:
        # branching
        if fmap[key] > max_count:
            max_num = key
            max_count = fmap[key]

    # return
    return max_num   
