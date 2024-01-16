# PART A
import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList: # When making functions, remmeber you are tring to createa dynamic array from a static array
    def __len__(self):
        return self.n
    
    def is_empty(self):
        return len(self) == 0

    def resize(self, new_size):
        temp_arr = make_array(new_size)
        for i in range(self.n):
            temp_arr[i] = self.data_arr[i]
        self.data_arr = temp_arr
        self.capacity = new_size

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def extend(self, iter_collection):
        for each in iter_collection:
            self.append(each)

    def pop(self, ind):  # this pop() method does not support negative index
        if (ind >= 0 and ind <= (self.n - 1)):
            for i in range(ind, len(self) - 1):
                self[i] = self[i + 1]
            self[len(self) - 1] = None
            self.n -= 1

            return self
        else:
            raise IndexError("Index out of range!")

    def __iter__(self):
        for i in range(self.n):
            yield self.data_arr[i]

    def __repr__(self):
        data_as_strings = [str(self.data_arr[i]) for i in range(self.n)]
        return '[' + ', '.join(data_as_strings) + ']'
    

    """
    Modify the methods below
    """
    

    def __iadd__(self, other): # part a
        # adjust variables
        self.extend(other)

        # return
        return self
    
    def __getitem__(self, ind): # part b
        if ind < 0:
            ind += self.n
        
        if (0 <= ind <= (self.n - 1)):
            return self.data_arr[ind]
        
        else:
            raise IndexError("Index out of range!")

    def __setitem__(self, ind, val): # part b
        if ind < 0:
            ind += self.n
        
        if (0 <= ind <= (self.n - 1)):
            self.data_arr[ind] = val

        else:
            raise IndexError("Index out of range!")

    def __mul__(self, other): # part c
        # variable
        new_array = ArrayList()

        # for-loop
        for iteration in range(other):
            for item in self:
                new_array += item

        # return
        return new_array

    def __rmul__(self, other): # part d
        # # variable
        # new_array = ArrayList()

        # # for-loop
        # for iteration in range(other):
        #     for item in self:
        #         new_array.append(item)

        # return
        return self * other

    def __init__(self, iter_collection = None): # part e
        self.data_arr = make_array(1)
        self.n = 0
        self.capacity = 1
        
        # branching
        if iter_collection != None:
            # for-loop
            for item in iter_collection:
                self.append(item)

    def remove(self, val): # part f
        # branching
        if val not in self:
            raise ValueError(f"Value '{val}' is not in ArrayList")
        
        # for-loop
        for i in range(self.n):
            if self[i] == val:
                self.pop(i)

        # return
                return

    def removeAll(self, val): # part g
        # branching
        if val not in self:
            raise ValueError(f"Value '{val}' is not in ArrayList")
        
        # pointers
        j = 0

        # for-loop
        for i in range(self.n):
            # branching
            if self[i] != val:
                # branching
                self[i], self[j] = self[j], self[i]

                # adjust variable
                j += 1

            # while-loop
            while (not self.is_empty()) and (self[-1] == val):
                self.pop()
