# import
from Lab6 import *

# a
  # a)
def min_max_BST(bst):
    '''
    Returns a tuple containing the min and max keys in the
    binary search tree
    '''
    # variables
    minimum = bst.root
    maximum = bst.root

    # while-loop --> adjust minimum
    while minimum.left is not None:  # leftmost is minimum
        minimum = minimum.left

    # while-loop --> adjust maximum
    while maximum.right is not None:  # rightmost is maximum
        maximum = maximum.right

    # return
    return (minimum.item.key, maximum.item.key) #.item allows access to the 'data' (key-value pair), while .key allows access to the key 

  # b)
'''In a Binary Search Tree, for any given key, every key to the left of the 
current key is smaller, and every key to the right is larger. Therefore, we 
know that we can keep traversing to the left to find the minimum key, and to 
the right to find the maximum key.

In a LinkedBinaryTree, because there are no such rules on where a value is 
supposed to be, we cannot find the minimum and maximum values unless we look 
at every single node. Therefore, the worst-case runtime would be O(n), where 
n is the number of nodes in the tree.
'''

  # c)
def min_max_BT(root):
    # branching
    if (root.left == None) and (root.right == None):
        # return
        return (root.data, root.data)
    
    elif (root.left == None):
        # variable
        r = min_max_BT(root.right)

        # return
        return min(root.data, r[0]), max(root.data, r[1])
    
    elif (root.right == None):
        # variable
        l = min_max_BT(root.left)

        # return
        return min(root.data, l[0]), max(root.data, l[1])
    
    else:
        # variables
        l = min_max_BT(root.left)
        r = min_max_BT(root.right)

        # return
        return min(root.data, l[0], r[0]), max(root.data, l[1], r[1])

# b
def first_unique(lst):
    # varaibles
    fmap = {}

    # for-loop
    for num in lst:
        # branching
        if num not in fmap:
            fmap[num] = 0
        fmap[num] += 1
    
    # for-loop --> to find the first unique number
    for num in lst:
        # branching
        if fmap[num] == 1:  # first unique number
            return num
