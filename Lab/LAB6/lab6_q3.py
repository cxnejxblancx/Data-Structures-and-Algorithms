# import
from Lab6 import *

# a
def compare_BST(bst1, bst2):
    ''' Returns true if the two binary search trees contain the
    same set of elements and false if not
    '''
    # Since a BST's inorder is sorted, we can just compare the inorders

    # branching --> check the length first (dead giveaway if they don't have the same values)
    if len(bst1) != len(bst2):
        # return
        return False

    # variables
    inorder1 = [key for key in bst1]
    inorder2 = [key for key in bst2]

    # return
    return (inorder1 == inorder2)

# b
def two_sum(lst, target):  # (key, val) = (num, index)
    # variable
    seen = {}

    # for-loop
    for i in range(len(lst)):
        # branchin
        if target - lst[i] in seen:
            return (seen[target - lst[i]], i)
        
        # adjust variable
        seen[lst[i]] = i
    
    # return
    return (None, None)
    
