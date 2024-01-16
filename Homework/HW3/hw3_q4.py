# import
from ArrayStack import *

class Queue:
    # initializer
    def __init__(self):
        # attributes
        self.data = ArrayStack()
        self.queue = ArrayStack()

    def __len__(self):
        # return
        return len(self.queue)
    
    def is_empty(self):
        # return
        return (len(self.queue) == 0)
    
    def enqueue(self, e): # e = 4 --> self.queue = [3, 2, 1], self.data = [1, 2, 3], self.data = [1, 2, 3, 4], self.queue = [4, 3, 2, 1]
        # branching
        if self.queue.is_empty():
            # adjust attribute
            self.queue.push(e)
        
        else:
            # while-loop
            while not self.queue.is_empty():
                # adjust attribute
                self.data.push(self.queue.pop())
            
            # adjust attribute
            self.data.push(e)

            # while-loop
            while not self.data.is_empty():
                # adjust attribute
                self.queue.push(self.data.pop())

    def first(self):
        # exception
        if self.queue.is_empty():
            raise Exception("Queue is empty!")
        
        # return
        return self.queue.top()

    def dequeue(self): # self.queue stack is reversed, so the first element entered into the self.data will be removed first        # exception
        if self.queue.is_empty():
            raise Exception("Queue is empty!")

        # return
        return self.queue.pop()
