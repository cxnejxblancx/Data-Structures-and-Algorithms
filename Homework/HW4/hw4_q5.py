# import
from LinkedBinaryTree import *

def is_height_balanced(bin_tree):
    # branching -- account for empty binary trees and those with only a root
    if (len(bin_tree) == 0) or (len(bin_tree) == 1):
        return True
    
    # helper function
    def sub_height(sub_tree):
        # branching
        if (sub_tree.left == None) or (sub_tree.right == None):
            if (sub_tree.left == None) and (sub_tree.right == None): # base case
                # return
                return 1
        
            elif (sub_tree.left == None):
                # variable --> recursion
                right_height = sub_height(sub_tree.right)

                # branching --> check if subtree is balanced
                if right_height == 1: # since the right child/node is not None, the only way the subtree can be balanced is if it's height is 1
                    # return --> continue calculations
                    return 1 + right_height

                else:
                    # return
                    return False

            
            elif (sub_tree.right == None):
                # variable --> recursion
                left_height = sub_height(sub_tree.left)

                # branching --> flag --> check if subtree is balanced
                if left_height == 1: # since the left child/node is not None, the only way the subtree can be balanced is if it's height is 1
                    # return --> continue calculations
                    return 1 + left_height
                
                else:
                    return False
                
        else:
            # variables --> recursion
            left_height = sub_height(sub_tree.left)
            right_height = sub_height(sub_tree.right)

            # branching --> flag --> check if subtree is balanced
            if abs(left_height - right_height) <= 1:
                # return --> continue calculations
                return 1 + max(left_height, right_height)

            else:
                # return
                return False
            
    # branching --> account for binary trees with a root with only one child
    if bin_tree.root.left == None:
        # variable --> recursion
        right_ht = sub_height(bin_tree.root.right)

        # branching
        if right_ht == 1: # since the right child/node is not None, the only way the subtree can be balanced is if it's height is 1
            # return
            return True 
        
        else:
            # return
            return False
        
    elif bin_tree.root.right == None:
        # variable --> recursion
        left_ht = sub_height(bin_tree.root.left)

        # branching
        if left_ht == 1: # since the left child/node is not None, the only way the subtree can be balanced is if it's height is 1
            # return
            return True 
        
        else:
            # return
            return False

    # variables --> recursion 
    left_ht = sub_height(bin_tree.root.left)
    right_ht = sub_height(bin_tree.root.right)

    # branching
    if abs(left_ht - right_ht) <= 1:
        return True
    
    else:
        return False
    
