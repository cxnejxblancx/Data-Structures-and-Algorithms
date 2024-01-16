def fibs(n): # generator
    # variables
    first = 1
    second = 1

    # for-loop
    for iteration in range(0, n):
        # branching
        if iteration == 0:
            yield 1
            
        elif iteration == 1:
            yield 1

        else:
            # variable
            sum = first + second

            # adjust variables
            first = second
            second = sum

            # yield
            yield sum
