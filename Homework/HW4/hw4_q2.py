# import
from DoublyLinkedList import *

# shallow copy
def copy_linked_list(lnk_lst):
    # variable
    shallow_copy = DoublyLinkedList()

    # while-loop
    for node in lnk_lst:
        shallow_copy.add_last(node)

    # return
    return shallow_copy

# deep copy
def deep_copy_linked_list(lnk_lst):
    # variables
    deep_copy = DoublyLinkedList()
    curr_node = lnk_lst.header.next

    # while-loop
    while curr_node != lnk_lst.trailer:
        # branching
        if isinstance(curr_node.data, int):
            deep_copy.add_last(curr_node.data)
        
        else:
            # variable --> recursion
            nested = deep_copy_linked_list(curr_node.data)

            # adjust variable
            deep_copy.add_last(nested)

        # adjust variable
        curr_node = curr_node.next

    # return
    return deep_copy
