# a
def __getitem__(self, i): # Worst-case runtime == theta(n/2) == theta(n), we can't do better
    """
    Return the vlaue at the ith node. If i is out of range,
    and IndexError is raised
    """
    # exception
    if not (0 <= i <= (self.size - 1)):
        raise IndexError("ERROR! Enter a valid index")
    
    # branching --> optimization
    if 0 <= i <= (self.size // 2):
        # variable
        curr_node = self.header.next

        # for-loop
        for iteration in range(i):
            curr_node = curr_node.next

        # return
        return curr_node.data
    
    else:
        # variable
        curr_node = self.trailer.prev
        num_iterations = (self.size - i) - 1

        # for-loop
        for iteration in range(num_iterations):
            curr_node = curr_node.prev

        # return
        return curr_node

# b
def bt_contains(root, val):
    '''
    Returns True if val exists in the binary tree and
    false if not
    '''
    # branching
    if root == None:
        return False
    
    if root.data == val:
        return True
    
    else:
        if bt_contains(root.left) or bt_contains(root.right):
            return True
        else:
            return False
