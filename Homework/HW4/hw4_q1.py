# import
from DoublyLinkedList import *

class CompactString:
        def __init__(self, orig_str): # 'aaaaabbbaaac' --> (a,5), (b,3), (a, 3), (c, 1)
            ''' 
            Initializes a CompactString object representing the string
            given in orig_str
            '''
            # attribute
            self.compstring = DoublyLinkedList()

            # branching --> account for empty original string
            if len(orig_str) != 0:
                # variables
                curr_char = orig_str[0] # 'a'
                char_count = 0

                # for-loop
                for index in range(len(orig_str)):
                    # branching
                    if orig_str[index] == curr_char:
                        char_count += 1

                    else: # index = 5, index = 8, index = 11
                        self.compstring.add_last((curr_char, char_count)) # ('a', 5), ('b', 3), ()
                        curr_char = orig_str[index] # 'b', 'a', 
                        char_count = 1

                    # branching --> if character is the last one in orig_str, put it in the not
                    if index == len(orig_str) - 1:
                        self.compstring.add_last((curr_char, char_count)) # ('a', 5), ('b', 3), ()


        def __add__(self, other):
            ''' 
            Creates and returns a CompactString object that represent
            the concatenation of self and other, also of type CompactString
            '''
            # variables
            new_comp = CompactString("")
            last_self = self.compstring.trailer.prev

            curr_node1 = self.compstring.header.next
            curr_node2 = other.compstring.header.next

            # branching --> account for empty compstring
            if (len(self.compstring) == 0) or (len(other.compstring) == 0):
                if (len(self.compstring) == 0) and (len(other.compstring) == 0):
                    # return
                    return new_comp
                
                elif len(self.compstring) == 0:
                    # for-loop
                    for node in other.compstring:
                        # adjust variable
                        new_comp.compstring.add_last(node)

                    # return
                    return new_comp

                elif len(other.compstring) == 0:
                    # for-loop
                    for node in self.compstring:
                        # adjust variable
                        new_comp.compstring.add_last(node)

                    # return
                    return new_comp

            # while-loop --> add the data in the first compstring to the new compstring
            while curr_node1 != last_self:
                new_comp.compstring.add_last(curr_node1.data)
                curr_node1 = curr_node1.next

            # branching --> check if the last character in the first compstring is the first in the second compstring
            if last_self.data[0] == curr_node2.data[0]:
                # variables
                char = curr_node2.data[0]
                num_chars = last_self.data[1] + curr_node2.data[1]

                # adjust variable
                new_comp.compstring.add_last((char, num_chars))
            
                # adjust variable
                curr_node2 = curr_node2.next

            else:
                # adjust variable
                new_comp.compstring.add_last(last_self.data)

            # while-loop --> add the data in the second compstring to the new compstring
            while curr_node2 != other.compstring.trailer:
                # adjust variable
                new_comp.compstring.add_last(curr_node2.data)
                curr_node2 = curr_node2.next

            # return
            return new_comp

        def __lt__(self, other):
            '''
            returns True if”f self is lexicographically less than
            other,also of type CompactString
            '''
            # variables
            curr_node_self = self.compstring.header.next
            curr_node_other = other.compstring.header.next
            
            # while-loop
            while (curr_node_self != self.compstring.trailer) and (curr_node_other != other.compstring.trailer):
                # branching
                if curr_node_self.data[0] < curr_node_other.data[0]: # aa, aaa
                    return True
                
                elif curr_node_self.data[0] > curr_node_other.data[0]: # aa, aa OR aaa, aa
                    return False
                
                else:
                    # branching --> account for compstrings of different lengths
                    if (curr_node_self.next == self.compstring.trailer) and (curr_node_other.next != other.compstring.trailer):
                        return True
                    
                    elif (curr_node_self.next != self.compstring.trailer) and (curr_node_self.next == self.compstring.trailer):
                        return False
                    
                    elif (curr_node_self.next == self.compstring.trailer) and (curr_node_other.next == other.compstring.trailer):
                        # branching --> account for difference in number of chars
                        if curr_node_self.data[1] < curr_node_other.data[1]:
                            return True
                        
                        else:
                            return False
                    
                    else: # the next nodes for neither compstring is the trailer
                        if curr_node_self.data[1] > curr_node_other.data[1]:
                            if curr_node_other.next.data[0] > curr_node_self.data[0]:
                                return True
                            else:
                                return False
                            

                        elif curr_node_self.data[1] < curr_node_other.data[1]:
                            if curr_node_self.next.data[0] < curr_node_other.data[0]:
                                return True
                            else:
                                return False
                            
                        else:
                            # adjust variables
                            curr_node_self = curr_node_self.next
                            curr_node_other = curr_node_other.next

            # branching --> account for one or both being the trailer
            if (curr_node_self == self.compstring.trailer) and (curr_node_other == other.compstring.trailer):
                # reutrn
                return False
            
            elif (curr_node_self == self.compstring.trailer):
                # return
                return True
            
            else:
                # return
                return False

        
        def __le__(self, other):
            '''
            returns True if”f self is lexicographically less than or
            equal to other, also of type CompactString
            '''
            # variables
            curr_node_self = self.compstring.header.next
            curr_node_other = other.compstring.header.next
            
            # while-loop
            while (curr_node_self != self.compstring.trailer) and (curr_node_other != other.compstring.trailer):
                # branching
                if curr_node_self.data[0] < curr_node_other.data[0]: # ab, ba 
                    return True
                
                elif curr_node_self.data[0] > curr_node_other.data[0]: # ba, ab
                    return False
                
                else:
                    # branching --> account for compstrings of different lengths
                    if (curr_node_self.next.data == self.compstring.trailer) and (curr_node_other.next != other.compstring.trailer):
                        return True
                     
                    elif (curr_node_self.next != self.compstring.trailer) and (curr_node_self.next == self.compstring.trailer):
                        return False
                    
                    elif (curr_node_self.next == self.compstring.trailer) and (curr_node_other.next == other.compstring.trailer):
                        # branching --> account for difference in number of chars
                        if curr_node_self.data[1] <= curr_node_other.data[1]:
                            return True
                        
                        else:
                            return False
                    
                    else: # the next nodes for neither compstring is the trailer, but both of the the first chars are the same
                        # branching --> account for difference in number of chars
                        if curr_node_self.data[1] > curr_node_other.data[1]: # if the first compact string has more of the chars than the second
                            if curr_node_other.next.data[0] > curr_node_self.data[0]: # if the next char in the second compact string is larger than the current char
                                return True
                            else:
                                return False
                            

                        elif curr_node_self.data[1] < curr_node_other.data[1]: # if the first compact string has less of the chars than the second
                            if curr_node_self.next.data[0] < curr_node_other.data[0]: # if the next char in the firs compact string is larger than the current char
                                return True
                            else:
                                return False
                            
                        else: # if the first compact string has the same amount of the chars as the second
                            # adjust variables
                            curr_node_self = curr_node_self.next
                            curr_node_other = curr_node_other.next

            # branching --> account for one being the trailer
            if (curr_node_self == self.compstring.trailer) and (curr_node_other == other.compstring.trailer):
                # return
                return True
            
            elif (curr_node_self == self.compstring.trailer):
                # return
                return True
            
            else:
                # return
                return False

        
        def __gt__(self, other):
            '''
            returns True if”f self is lexicographically greater than
            other, also of type CompactString
            '''
            # return
            return not (self <= other)
        
        def __ge__(self, other):
            '''
            returns True if”f self is lexicographically greater than or
            equal to other, also of type CompactString
            '''
            # return
            return not (self < other)
        
        def __repr__(self):
            '''
            Creates and returns the string representation (of type str)
            of self
            '''
            # variable
            string = ""

            # for-loop --> adjust variable
            for node in self.compstring:
                string += (node[0] * node[1])

            # return
            return string
