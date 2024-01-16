# import
from Lab5_DoublyLinkedList import *

# a
class LinkedStack:
    def __init__(self):
        # attributes
        self.data = DoublyLinkedList()

    def __len__(self):
        '''
        Returns the number of elements in the stack.
        '''
        # return
        return len(self.data)

    def is_empty(self):
        ''' 
        Returns true if the stack is empty,false otherwise. 
        '''
        # return
        return len(self.data) == 0

    def push(self, e):
        ''' 
        Adds an element, e, to the top of the stack.
        '''
        # adjust
        self.data.add_last(e)

    def top(self):
        '''
        Returns the element at the top of the stack.
        An exception is raised if the stack is empty.
        '''
        # exception
        if self.is_empty:
            raise Exception("The stack is empty!")
        
        # return
        return self.data.trailer.prev.data

    def pop(self):
        '''
        Removes and returns the element at the top of the stack.
        An exception is raised if the stack is empty.
        '''
        # exception
        if self.data.is_empty:
            raise Exception("The stack is empty!")

        # return
        return self.data.delete_last()

# b
def bt_even_sum(root):
    '''
    Returns the sum of all even integers in the binary
    tree
    '''
    # branching
    if (root.left == None) and (root.right == None):
        if root.data % 2 == 0:
            return root.data
        else:
            return 0
    
    elif (root.left == None):
        if root.data % 2 == 0:
            return root.data + bt_even_sum(root.right)
        else:
            return bt_even_sum(root.right)
    
    elif (root.right == None):
        if root.data % 2 == 0:
            return root.data + bt_even_sum(root.left) + bt_even_sum(root.right)
        
        else:
            return bt_even_sum(root.left) + bt_even_sum(root.right)
    
