# import
from Lab4_ArrayStack import ArrayStack
from Lab4_ArrayQueue import ArrayQueue

# b
class MeanQueue:
    def __init__(self):
        self.data = ArrayQueue()
        self.queuesum = 0

    def __len__(self):
        '''Return the number of elements in the queue'''
        # return
        return len(self.data)

    def is_empty(self):
        ''' Return True if queue is empty'''
        # return
        return self.data.is_empty()

    def enqueue(self, e):
        ''' Add element e to the front of the queue. If e is not an int or float, raise a TypeError '''
        # branching
        if not isinstance(e, int) or isinstance(e, float):
            raise TypeError("Invalid input! Must be an integer or a float")
        
        # adjust
        self.data.enqueue(e)
        self.queuesum += e
        

    def dequeue(self):
        ''' Remove and return the first element from the queue. If the queue is empty, raise an exception'''
        # branching
        if self.is_empty():
            raise Exception("Mean quene is empty!")
        
        # variable
        target = self.data.dequeue()

        # adjust
        self.queuesum -= target

        # return
        return target


    def first(self):
        ''' Return a reference to the first element of the queue without removing it. If the queue is empty, raise an exception '''
        # branching
        if self.data.is_empty():
            raise Exception("Mean queue is empty!")
        
        # return
        return self.data.first()

    def sum(self): # O(1) RUNTIME --> adjust initializer and other functions as follows to calculate sum
        ''' Returns the sum of all values in the queue'''
        # return
        return self.queuesum
        
    def mean(self):
        ''' Return the mean (average) value in the queue'''
        # branching
        if self.data.is_empty():
            raise ZeroDivisionError("Mean queue is empty! Cannot find the average.")
        
        # variable
        mean = self.queuesum / len(self)

        # return
        return mean

# a
def stack_sum(s):
    """
    : s type: ArrayStack
    : return type: int
    """
    # branching
    if len(s) == 1:
        return s.top()
    else:
        return s.pop() + stack_sum(s)
      
