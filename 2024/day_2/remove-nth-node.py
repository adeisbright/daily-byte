'''
Given a linked list and a value n, 
remove the nth to last node and return the resulting list.

Ex: Given the following linked lists...

1->2->3->null, n = 1, return 1->2->null
1->2->3->null, n = 2, return 1->3->null
1->2->3->null, n = 3, return 2->3->null
'''
class Node:
    def __init__(self , value) :
        self.value = value 
        self.next = None 


class LinkedList:
    def __init__(self):
        self.length = 0 
        self.head = None 
        self.tail = None 
    
    def append(self,item):
        node = Node(item)
        if self.head is None:
            self.head = node 
        elif self.tail:
            self.tail.next = node 
        self.tail = node 
        self.length += 1 
    
    def removeNthItem(self , n):
        current_node = self.head 
        print(current_node.value)
        loop_control = n 
        count_start = 1
        previous_node = None 
        while current_node:
            if loop_control == count_start:
                if previous_node is not None: 
                    previous_node.next = current_node.next 
                else:
                    self.head = current_node.next
                return self.head 
            count_start += 1 
            previous_node = current_node 
            current_node = current_node.next 
    def show(self ):
        current = self.head 
        linked_items = ""
        while current is not None:
            linked_items += str(current.value) + "->"
            current = current.next 

        print(linked_items + "null") 
        
if __name__ == "__main__":
    ll = LinkedList() 
    ll.append(1) 
    ll.append(2)
    ll.append(3)
    ll.show()
    ll.removeNthItem(1)
    ll.show()





