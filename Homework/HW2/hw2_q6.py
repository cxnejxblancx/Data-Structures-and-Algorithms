   # a
def count_lowercase(s, low, high):
    # branching
    if low > high: # base case
        return 0

    else: # recursive case
        # branching --> Check if character in string is lowercase or uppercase
        if 'a' <= s[low] <= 'z': # If character is lowercase, add 1 to the REST (overall sum)
            rest = 1 + count_lowercase(s, (low + 1), high)
        else: # Otherwise, disregard and continuing checking the REST of the characters
            rest = count_lowercase(s, (low + 1), high)

        # return
        return rest
    

    # b
def is_number_of_lowercase_even(s, low, high):
    # flag
    is_even = False

    # branching
    if count_lowercase(s, low, high) % 2 == 0:
        # adjust flag
        is_even = True

    # return
    return is_even
