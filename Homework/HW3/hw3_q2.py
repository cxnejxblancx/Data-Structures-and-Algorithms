# import
from ArrayStack import ArrayStack

class MaxStack:
    # initializer
    def __init__(self):
        # attributes
        self.data = ArrayStack()
        self.max_val = None

    def is_empty(self):
        # return
        return (len(self.data) == 0)
    
    def __len__(self):
        # return
        return len(self.data)
    
    def push(self, e):
        # branching --> adjust attribute
        if self.is_empty():
            self.max_val = e

        else:
            # branching --> adjust attribute
            if self.max_val < e:
                self.max_val = e

            else:
                self.max_val = self.data.top()[1]

        # adjust attribute
        self.data.push((e, self.max_val))

    def top(self):
        # exception
        if self.is_empty():
            raise Exception("Max Stack is empty!")
        
        # return
        return self.data.top()[0]

    def pop(self):
        # exception
        if self.is_empty():
            raise Exception("Max Stack is empty!")

        # variable
        target = self.data.pop()

        # branching --> adjust attribute
        if self.is_empty():
            self.max_val = None
        
        else:
            self.max_val = self.data.top()[1]

        # return  
        return target[0]
    
    def max(self):
        # exception
        if self.is_empty():
            raise Exception("Max Stack is empty!")
        
        # return
        return self.max_val
