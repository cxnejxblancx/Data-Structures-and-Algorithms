# import
from Lab4_ArrayStack import ArrayStack
from Lab4_ArrayQueue import ArrayQueue

# a
def eval_prefix(exp_str):
    """
    : exp type: str
    : return type: int
    """
    # adjust variable
    exp_lst = exp_str.split( ) # ["-", "+", "*", "16", "5", "*", "8", "4", "20"]

    # variable
    stack = ArrayStack()

    # for-loop
    for index in range((len(exp_lst)-1), -1, -1):
        # branching
        if exp_lst[index].isdigit():
            # adjust variable
            stack.push(exp_lst[index])

        else:
            # branching
            if index == 0:
                # variables
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())
                operator = exp_lst[index]
            
            else:
                # variables
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                operator = exp_lst[index]


            # branching
            if operator == "+":
                result = operand1 + operand2

            elif operator == "-":
                result = operand1 - operand2

            elif operator == "*":
                result = operand1 * operand2

            elif operator == "/":
                if operand2 == 0:
                    raise ZeroDivisionError
                else:
                    result = operand1 / operand2

            # adjust variable
            stack.push(result)

    # return
    return stack.pop()

# b
def flatten_list_by_depth(lst):
    """
    : lst type: list
    : return type: list
    """
    # variables
    queue = ArrayQueue()
    new_lst = []
    
    # for-loop
    for elem in lst:  # copy all elem from lst to queue
        queue.enqueue(elem)

    # while-loop
    while not queue.is_empty():
        # variable
        front = queue.dequeue()

        # branching
        if isinstance(front, list):
            for elem in front:   # take off one layer of nesting
                queue.enqueue(elem)  # put all elem back into the end of queue

        elif isinstance(front, int):
            new_lst.append(front)  # append to new lst, don't put back into queue

    # return
    return new_lst
  
