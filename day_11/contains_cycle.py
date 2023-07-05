'''
EXAMPLE 1
---------- 
Given a linked list, containing unique numbers, 
return whether or not it has a cycle.
Note: a cycle is a circular arrangement (i.e. one node points back to a previous node)

Ex: Given the following linked lists...

1->2->3->1 -> true (3 points back to 1)
1->2->3 -> false
1->1 true (1 points to itself)
'''

'''
EXAMPLE 2 
----------- 
Given a potentially cyclical linked list where each value is unique, 
return the node at which the cycle starts. 
If the list does not contain a cycle, 
return null.

Ex: Given the following linked lists...

1->2->3, return null
1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
1->9->3->7->7 (7 points to itself), return a reference to the node containing 7

'''
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from day_7.linked_list import LinkedList
    else:
        from day_7.linked_list import LinkedList


class CyclicLinkedList(LinkedList):
    def __init__(self) -> None:
        super().__init__()

    def is_there_cycle(self):
        list_set = set() 
        current = self.head 

        while current:
            if current.value in list_set:
                return True 
            else:
                list_set.add(current.value) 
            current = current.next 
            

        return False 
    
    def get_cycle_index(self):
        list_set = set() 
        current = self.head 
        previous = None 

        while current:
            if current.value in list_set:
                return previous.value 
            else:
                list_set.add(current.value)

            previous = current 
            current = current.next 

        return None 
    

if __name__ == "__main__":
    ll = CyclicLinkedList() 

    ll.append(1) 
    ll.append(9) 
    ll.append(3) 
    ll.append(7) 
    ll.append(7) 

    cyclic_index = ll.get_cycle_index() 

    print(cyclic_index)
