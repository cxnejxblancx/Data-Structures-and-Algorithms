class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imaginary = b


    def __add__(self, other):
        # calculations
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary

        # object-casting
        sum = Complex(real_sum, imaginary_sum)

        # return
        return sum


    def __sub__(self, other):
        # calculations
        real_sub = self.real - other.real
        imaginary_sub = self.imaginary - other.imaginary

        # object-casting
        sub = Complex(real_sub, imaginary_sub)

        # return
        return sub
    

    def __mul__(self, other):
        # calculations
        first = self.real * other.real
        outer = self.real * other.imaginary
        inner = self.imaginary * other.real
        last = -(self.imaginary * other.imaginary)

        real_prod = first + last
        imaginary_prod = outer + inner

        # object-casting
        prod = Complex(real_prod, imaginary_prod)
 
        # return
        return prod
    

    def __str__(self):
        # branching
        if self.imaginary > 0:
            str_rep = f"{self.real} + {self.imaginary}i"

        elif self.imaginary < 0:
            str_rep = f"{self.real} - {abs(self.imaginary)}i"

        # return
        return str_rep
    

    def __iadd__(self, other):
        # calculations
        self = self + other

        # return
        return self
