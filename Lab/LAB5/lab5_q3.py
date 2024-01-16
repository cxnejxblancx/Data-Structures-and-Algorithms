# import
from Lab5_DoublyLinkedList import DoublyLinkedList

# a
class MidStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.mid = None  # starts off None for empty DLL

    def __len__(self):
        '''
        Returns the number of elements in the stack.
        '''
        # return
        return len(self.data)
    
    def is_empty(self):
        '''
        Returns true if stack is empty and false otherwise.
        '''
        # return
        return len(self) == 0
    
    def push(self, e):
        '''
        Adds an element, e, to the top of the stack.
        '''
        # adjust variable
        self.data.add_last(e)  # add to top of stack

        # branching
        if len(self) == 1:  # only 1 element (was empty before)
            self.mid = self.data.trailer.prev #mid is last node 
        
        elif len(self) % 2 != 0:  # if len is odd, bump pointer up
            self.mid = self.mid.next
        

    def pop(self):
        '''
        Returns the element at the top of the stack. An exception
        is raised if the stack is empty.
        '''
        # exception
        if self.is_empty():
            raise Exception("Stack is empty!")
        
        # variable
        val = self.data.delete_last()

        # branching 
        if self.is_empty():
            self.mid = None

        elif len(self) % 2 == 0:  # if len is even, bump pointer down
            self.mid = self.mid.prev
        
        # return
        return val

    def top(self):
        '''
        Removes and returns the element at the top of the stack. An
        exception is raised if the stack is empty.
        '''
        # exception
        if self.is_empty():
            raise Exception("Stack is empty!")
        
        # return
        return self.data.trailer.prev.data

    def mid_push(self, e):
        '''
        Adds an element, e, to the middle of the stack. An exception
        is raised if the stack is empty.
        '''
        # exception
        if self.mid is None:
            raise Exception("Stack is empty!")
        
        # adjust variable
        self.data.add_after(self.mid, e)  # add to top of stack

        # branching
        if len(self) % 2 != 0:  # if len is odd, bump pointer up
            self.mid = self.mid.next

# b
def is_perfect(root):
    ''' Returns True if the Binary Tree is perfect and
    false if not using recursion'''
    # branching
    if (root.left == None) and (root.right == None):  # leaf node
        return (True, 0)  # height of a leaf node is 0
    
    elif (root.left is None) or (root.right is None):  # only has 1 child
        return (False, -1)  # if we're returning False, height doesn't matter
    
    # variables --> recursion
    l_perfect, l_height = is_perfect(root.left)
    r_perfect, r_height = is_perfect(root.right)

    # branching
    if (l_perfect and r_perfect) and (l_height == r_height):
        return (True, l_height + 1)
    
    else:
        return (False, -1)  # height doesn't matter from here
    
