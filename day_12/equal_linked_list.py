'''
You are given the pointer to the head nodes of two linked lists. 
Compare the data in the nodes of the linked lists to check if they are equal. 
If all data attributes are equal and the lists are the same length, return . 
Otherwise, return .

Example
llist1 = 1->2->3->None 
llist2 = 1->2->3->4->None 

The two lists have equal data attributes for the first  3 nodes.  
llist is longer, though, so the lists are not equal. Return 0

'''

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from day_7.linked_list import LinkedList
    else:
        from day_7.linked_list import LinkedList


class EqualLinkedList(LinkedList):
    def __init__(self):
        super().__init__() 
    
    def compare_lists(self , llist1 , llist2):
        current_1 = llist1.head  
        current_2 = llist2.head  

        index_1 = 0 
        index_2 = 0 
       
        while current_1 or  current_2:
            if index_1 != index_2: return False 
            if current_1.value != current_2.value :return False 
            current_1 = current_1.next 
            current_2 = current_2.next 

            if current_1 : index_1 += 1 
            if current_2 : index_2 += 1 
        
        return True 
            
if __name__ == "__main__":

    ll1 = LinkedList() 
    ll2 = LinkedList() 

    ll1.append(1)
    ll1.append(2)
    ll1.append(3)

    ll2.append(1)
    ll2.append(2)
    ll2.append(3)
    # ll2.append(4)

    ll = EqualLinkedList() 
    test = ll.compare_lists(ll1 , ll2) 
    print(test)
    