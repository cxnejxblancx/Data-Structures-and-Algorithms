# import stack
from ArrayStack import *

def postfix_calculator():
    # input
    user_input = input("--> ")

    # variables
    stack = ArrayStack()
    operators = "+-*/"
    variables = {}

    # while-loop
    while user_input != "done()":
        # adjust variable
        input_lst = user_input.split() # ['x', '=', '5', '1', '-']

        # variable
        var = None

        # branching --> if storing a variable, adjust input_lst as such
        if '=' in input_lst:
            var = input_lst[0]

            if input_lst[1] == '=':
                input_lst = input_lst[2:] 

        # adjust variable --> reverse input_lst
        input_lst = input_lst[::-1] #  --> ['-', '1', '5']
        
        # while-loop --> executed every time the user inputs
        while len(input_lst) != 0:
            # variable
            target = input_lst.pop()

            # branching --> determine what steps to takes for each type of target
            if target in operators:
                # variables
                operand2 = stack.pop()
                operand1 = stack.pop()

                # branching --> account for integers AND floats
                    # operand 1
                if operand1.isdigit():
                    operand1 = int(operand1)
                else:
                    operand1 = float(operand1)

                    # operand 2
                if operand2.isdigit():
                    operand2 = int(operand2)
                else:
                    operand2 = float(operand2)
                
                # branching --> account for each operator
                if target == "+":
                    result = operand1 + operand2

                elif target == "-":
                    result = operand1 - operand2

                elif target == "*":
                    result = operand1 * operand2

                elif target == "/":
                    if operand2 == 0:
                        raise ZeroDivisionError
                    else:
                        result = operand1 / operand2

                # adjust variable
                stack.push(str(result))

            else:
                if target in variables:
                    stack.push(variables[target])
                else:
                    stack.push(target)

        # branching
        if var != None:
            variables[var] = stack.pop()
            print(var)

        else:
            print(stack.pop())

        # input --> repeat loop for next input
        user_input = input("--> ")

postfix_calculator()
