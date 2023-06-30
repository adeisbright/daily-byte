'''
A linked list is a data structure 

There is a head and a Tail 
If there is only one item, then that item is both the tail and 

The item at the beggining is the head.
That at the end is the tail. 

You can add an item to the list, remove an item, find items. 

To remove an item to the end (tail) of the list O(1) 
The worst case scenario of adding at the end is O(N-1) 
The best case is adding at the tail. 
So,adding an item is O(N) 

Removing an item is also O(N)
Each item is a Node . 

A linked list has the following size : 
length , 
tail : The node at the end 
head : the node at the top 
''' 

class Node:
    def __init__(self , value):
        self.value = value 
        self.next = None 


class LinkedList:
    def __init__(self):
        self.length = 0 
        self.head = None 
        self.tail = None 
    
    def append(self,item):
        node = Node(item) 
        if not self.head:
            self.head = node 
        elif self.tail:
            self.tail.next = node
          

        self.tail = node 
        self.length += 1 
    def prepend(self,item):
        node = Node(item) 
        head = self.head 
        self.head = node 
        self.head.next = head 
        
        if not self.tail:
            self.tail = node 
      
        self.length += 1 
    
    def show(self):
        head = self.head 
        list_items = ""
        while head is not None:
            list_items += str(head.value) + "->"
            head = head.next
        print(list_items)

    def find(self , value):
        ''' Returns true if a value exists in a linked list ''' 

        if self.head is None : 
            return False

        head = self.head 
        while head:
            if head.value == value : 
                return True
            head = head.next 
        
        return False
    
    def delete(self , value):
        ''' Removes a value from  a linked list if it exists 
            To be able to delete an item from a linked list, we 
            basically need to re-assign the previous node 
            to replace the item to be deleted. 
            To achieve this, we will use two pointers one that always 
            points to the previous node, and one that points to the next node

        '''
        if self.head is None : 
            return None 
        
        current_node  = self.head 
        previous_node = None 

        while current_node:
            if current_node.value == value : 
                if previous_node:
                    previous_node.next = current_node.next 
                else:
                    self.head = current_node.next 
                return 
            
            previous_node = current_node 
            current_node = current_node.next 

if __name__ == "__main__":

    ll = LinkedList() 
    ll.append(5)
    ll.prepend(8)
   

    ll.append(6)
    ll.append(2)
    ll.show()
    ll.delete(5)
    ll.show()
    

    

