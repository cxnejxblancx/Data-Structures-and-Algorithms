# a
def move_zeros(nums):
    """
    : nums type: list[int]
    : return type: None
    """
    # variables
    zero_pointer = 0

    # for-loop
    for index in range(len(nums)):
        if nums[index] > 0:
            nums[index], nums[zero_pointer] = nums[zero_pointer], nums[index]
            zero_pointer += 1

    # return
    return nums

# b
def binary_search(lst, low, high, val):
    """
    : lst type: list[int]
    : val type: int
    : low type, high type: int : return type: int
    """
    # branching --> base case
    if low > high: # low will only ever be greater than high when the value is not in the list
        return -1
    
    # variable
    mid = (low + high) // 2

    # branching --> recursive cases
    if lst[mid] == val:
        index = mid
        return index
    
    elif lst[mid] < val:
        return binary_search(lst, (mid + 1), high, val)

    elif lst[mid] > val:
        return binary_search(lst, low, (mid - 1), val)
      
