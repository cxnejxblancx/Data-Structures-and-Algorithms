# import
from Lab6 import *

def is_BST(root):
    '''
    Returns True if the tree is a BST and False if not
    '''
    def is_bst_helper(root):
        # branching
        if root is None:
            return (None, None, True)  # min, max, bool
            
        # variables --> recursion
        lmin, lmax, lbst = is_bst_helper(root.left)
        rmin, rmax, rbst = is_bst_helper(root.right)
        
        # branching
        if not (lbst and rbst):  # if either of them is not bst -> not bst
            return (None, None, False)
            
        if lmax and lmax >= root.data:  # bigger value in the left -> not bst
            return (None, None, False)
            
        if rmin and rmin <= root.data:  # smaller value in the right -> not bst
            return (None, None, False)
            
        # if lmin is None:
        #     dmin = root.data
        # else:
        #     dmin = lmin

        # variables
        dmin = lmin or root.data
        dmax = rmax or root.data

        # return
        return (dmin, dmax, True)
    
    # return
    return is_bst_helper()
