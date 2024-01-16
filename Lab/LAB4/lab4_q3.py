# import
from Lab4_ArrayStack import ArrayStack

def flatten_list(lst): # ITERATIVE
    """
    : lst type: list
    : return type: None
    """
    # variable
    stack = ArrayStack()

    # while-loop
    while len(lst) != 0:
        # variable
        target = lst.pop() # remove last value from the lst

        # branching
        if isinstance(target, int): # if the value is an integer, push it in the stack
            """
            necessary to do this starting at the END of the list because since we are using
            a stack, it will REVERSE the order (LIFO)
            """
            stack.push(target)

        else: # otherwise, extend the list to get rid of ONE level of nesting within that value and continue to check the last value of the input list
            lst.extend(target)

    # while-loop --> add values from the stack back into the list
    while not stack.is_empty():
        lst.append(stack.pop())
