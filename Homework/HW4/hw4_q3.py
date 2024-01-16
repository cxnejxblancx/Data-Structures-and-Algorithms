# import
from DoublyLinkedList import *

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    # variables
    merged = DoublyLinkedList()
    curr_node1 = srt_lnk_lst1.header.next
    curr_node2 = srt_lnk_lst2.header.next

    # helper function
    def merge_sublists(curr_node1, curr_node2):
        # branching --> base cases
        if (curr_node1.data == None) or (curr_node2.data == None): # check if either node has reach the trailer
            # branching --> account for lists of different lengths or with greater values
            if (curr_node1 == None) and (curr_node2 == None): # case 1
                # return
                return
            
            if curr_node1.data == None: # case 2
                # while-loop
                while curr_node2.data != None:
                    merged.add_last(curr_node2.data)
                    curr_node2 = curr_node2.next

            elif curr_node2.data == None: # case 3
                # while-loop
                while curr_node1.data != None:
                    merged.add_last(curr_node1.data)
                    curr_node1 = curr_node1.next

            # return
            return

        # branching --> compare data
        if curr_node1.data < curr_node2.data:
            # adjust variables
            merged.add_last(curr_node1.data)
            curr_node1 = curr_node1.next

            # recursion
            merge_sublists(curr_node1, curr_node2)

        elif curr_node1.data > curr_node2.data:
            # adjust variable
            merged.add_last(curr_node2.data)
            curr_node2 = curr_node2.next

            # recursion
            merge_sublists(curr_node1, curr_node2)

        else:
            # adjust variables
            merged.add_last(curr_node1.data)
            merged.add_last(curr_node2.data)
            curr_node1 = curr_node1.next
            curr_node2 = curr_node2.next

            # recursion
            merge_sublists(curr_node1, curr_node2)

    # call helper function to update merged list
    merge_sublists(curr_node1, curr_node2)

    # return
    return merged
