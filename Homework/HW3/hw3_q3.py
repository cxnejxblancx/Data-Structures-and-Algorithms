# import
from ArrayStack import *
from ArrayDeque import *

class MidStack:
    # initializer
    def __init__(self):
        # attributes
        self.data = ArrayStack()
        self.double_ended = ArrayDeque()

    def __len__(self):
        # return
        return len(self.data)
    
    def is_empty(self):
        # return
        return (len(self.data) == 0)
    
    def push(self, e):
        # adjust attribute
        self.data.push(e)

    def top(self):
        # exception
        if self.is_empty():
            raise Exception("Max Stack is empty!")
        
        # return
        return self.data.top()

    def pop(self):
        # exception
        if self.is_empty():
            raise Exception("Max Stack is empty!")

        # variable
        return self.data.pop()

    def mid_push(self, e):
        # variable
        n = len(self)

        # branchiing --> account for an empty stack
        if n == 0:
            self.data.push(e)

        else:
            # branching -> variable
            if n % 2 == 0:
                mid = len(self) / 2

            else:
                mid = (len(self) + 1) / 2

            # variable
            num_vals_after_mid = int(n - mid)

            # for-loop
            for iteration in range(num_vals_after_mid):
                # adjust attributes
                target = self.data.pop()
                self.double_ended.enqueue_last(target)

            # adjust
            self.data.push(e)

            # while-loop
            while not self.double_ended.is_empty():
                # adjust attributes
                target = self.double_ended.dequeue_last()
                self.data.push(target)
            
