    # a
def powers_of_two(n):
    # for-loop
    for num in range(n):
        yield f"{2 ** num}" 

    # b
class Polynomial:
    def __init__(self, coefficients = [0]):
        """
        :type coefficients: list
        """
        self.coefficients = coefficients


    def __add__(self, other):
        """
        :type other: Polynomial 
        :return type: Polynomial
        """
        # import
        from copy import copy

        # variables
        self_copy = self.coefficients.copy()
        other_copy = other.coefficients.copy()
        coefficients = []

        # branching --> if self_copy is shorter, switch other_copy and self_copy
        if len(other_copy) > len(self_copy):
            self_copy, other_copy = other_copy, self_copy

        # for-loop
        for index in range(len(other_copy)):
            # calculation
            sum = self_copy[index] + other_copy[index]

            # adjust variable
            coefficients.append(sum)

        # adjust variable
        coefficients += self_copy[(len(other_copy)):]

        # object-casting
        new_poly = Polynomial(coefficients)

        # return
        return new_poly
        

    def __call__(self, param):
        """
        :type other: Polynomial 
        :return type: int
        """
        # variable
        sum = 0

        # for-loop
        for index in range(len(self.coefficients)):
            sum += (self.coefficients[index] * (param ** index))

        # return
        return sum
    

    def __mul__(self, other): 
        """
        :type other: Polynomial
        :return type: Polynomial object
        """
        # variable
        coefficients = [0] * (len(self.coefficients) + len(other.coefficients))

        # for-loop
        for index in range(len(self.coefficients)):
            for ind in range(len(other.coefficients)):
                coefficients[index + ind] += self.coefficients[index] + other.coefficients[ind]

        # return
        return Polynomial(coefficients)
                           

    def derive(self):
        """
        :return type: None
        """
        # for-loop
        for index in range(1, len(self.coefficients)):
            self.coefficients[index - 1] = self.coefficients[index] * index
        self.coefficients.pop()


    def __str__(self): 
        """
        : return type: str
        """
        # variable
        str_rep = f" + {self.coefficients[0]}"

        # for-loop
        for index in range(1, len(self.coefficients)):
            # branching
            if (self.coefficients[index] != 0) and (index != (len(self.coefficients) - 1)):
                str_rep = f" + {self.coefficients[index]}x^{index}" + str_rep

            elif index == (len(self.coefficients) - 1):
                str_rep = f"{self.coefficients[index]}x^{index}" + str_rep

        # return
        return str_rep           
    
