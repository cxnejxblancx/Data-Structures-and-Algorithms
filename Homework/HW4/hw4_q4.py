from LinkedBinaryTree import *

def min_and_max(bin_tree):
    # branching
    if len(bin_tree) == 0:
        raise Exception("Binary tree is empty!")

    # helper
    def subtree_min_and_max(root):
        # branching --> adjust min and max variables accordingly
        if (root.left == None) or (root.right == None):
            if (root.left == None) and (root.right == None):
                sub_min = root.data
                sub_max = root.data

            elif (root.left == None):
                # variable --> recursion
                right = subtree_min_and_max(root.right)
                
                # calculations
                sub_min = min(root.data, right[0])
                sub_max = max(root.data, right[1])

            elif (root.right == None):
                # variable --> recursion
                left = subtree_min_and_max(root.left)
                
                # calculations
                sub_min = min(root.data, left[0])
                sub_max = max(root.data, left[1])

        else:
            # variables --> recursion
            left = subtree_min_and_max(root.left)
            right = subtree_min_and_max(root.right)

            # calulations
            sub_min =  min(root.data, left[0], right[0])
            sub_max = max(root.data, left[1], right[1])
        
        # return
        return (sub_min, sub_max)
    
    # variable --> helper function call
    tree_data = subtree_min_and_max(bin_tree.root)

    # adjust variables
    minimum = tree_data[0]
    maximum = tree_data[1]

    # return
    return (minimum, maximum)
