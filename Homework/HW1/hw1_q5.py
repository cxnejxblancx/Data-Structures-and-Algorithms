class Vector:
    # a
    def __init__(self, d):
        if isinstance(d, int):
            self.coords = [0] * d 

        elif isinstance(d, list):
            self.coords = d

    def __len__(self):
        return len(self.coords)
    
    def __getitem__(self, j):
        return self.coords[j]
    
    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        
        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] + other[j]

        return result
    
    # b
    def __sub__(self, other):
        # branching
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        
        # variable
        result = Vector(len(self))

        # for-loop
        for j in range(len(self)):
            result[j] = self[j] - other[j]

        # result
        return result

    # c  
    def __neg__(self):
        # variable
        result = Vector(len(self))

        # for-loop
        for index in range(len(self)):
            result[index] = -self[index]

        # return
        return result

    # d, f
    def __mul__(self, multiplier):
        # branching
        if isinstance(multiplier, int):
            # variable
            result = Vector(len(self))

            # for-loop
            for index in range(len(self)):
                result[index] = self[index] * multiplier

        elif isinstance(multiplier, Vector):
            # variable
            result = 0

            # branching
            if (len(self) != len(multiplier)):
                raise ValueError("dimensions must agree")
            
            # for-loop
            for index in range(len(self)):
                result += self[index] * multiplier[index]
            
        # return
        return result
    
    # e
    def __rmul__(self, multiplier): # instead of (3 * v1), calculates (v1 * 3)
        # variable
        result = Vector(len(self))

        # for-loop
        for index in range(len(self)):
            result[index] = self[index] * multiplier

        # return
        return result
        
    def __eq__(self, other):
        return self.coords == other.coords
    
    def __ne__(self, other):
        return not (self == other)
    
    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'
    
    def __repr__(self):
        return str(self)
