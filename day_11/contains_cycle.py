'''
Given a linked list, containing unique numbers, 
return whether or not it has a cycle.
Note: a cycle is a circular arrangement (i.e. one node points back to a previous node)

Ex: Given the following linked lists...

1->2->3->1 -> true (3 points back to 1)
1->2->3 -> false
1->1 true (1 points to itself)
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
    

if __name__ == "__main__":
    ll = CyclicLinkedList() 

    ll.append(1) 
    ll.append(1) 

    is_cyclic = ll.is_there_cycle() 

    print(is_cyclic)
