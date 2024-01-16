def add_binary(bin_num1, bin_num2):
    """
    bin_num1 - type: str
    bin_num2 - type: str
    return value - type: str
    """
    # variables
    sum = ""
    carry = 0
    max_length = max(len(bin_num1), len(bin_num2))

    # sign extension so both will have the same length
    b1 = (max_length - len(bin_num1)) * '0' + bin_num1
    b2 = (max_length - len(bin_num2)) * '0' + bin_num2

    # for-loop
    for index in range(1, (max_length + 1)):
        # we will use the negative indices since we evaluate from right to left
        sum_bits = int(b1[-index]) + int(b2[-index]) + carry
        sum = str(sum_bits % 2) + sum

        # branching
        if sum_bits < 2:
            carry = 0
        else:
            carry = 1

    # return
    return carry * '1' + sum
