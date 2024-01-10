class Node:
    def __init__(self , value):
        self.value = value 
        self.next = None 


class LinkedList:
    def __init__(self) -> None:
        self.length = 0 
        self.head = None 
        self.tail = None 

    def append(self , item) :
        node = Node(item) 
        if not self.head:
            self.head = node 
        elif self.tail : 
            self.tail.next = node
        self.tail = node 
        self.length += 1 
    def prepend(self , item):
        node = Node(item) 
        head = self.head 
        self.head = node 
        self.head.next = head 
        if  not self.tail:
            self.tail = node 
        self.length += 1
    def show(self):
        current = self.head 
        linked_items = ""
        while current is not None:
            linked_items += str(current.value) + "->"
            current = current.next 

        print(linked_items + "null") 
    def find(self , item):
        current = self.head 
        while current is not None:
            if(current.value == item):
                return item
            current = current.next 

        return None
    
    def delete(self , item):
        current_node = self.head 
        previous_node = None
        while current_node is not None:
            if current_node.value == item:
                if previous_node:
                    previous_node.next = current_node.next 
                else:
                    self.head = current_node.next
                return 
            previous_node = current_node 
            current_node = current_node.next
    def insert_before(self , value , new_value):
        current_node = self.head 
        previous_node = None 
        while current_node is not None:
            if current_node.value == value:
                node = Node(new_value)
                node.next = current_node
                if previous_node:
                    previous_node.next = node 
                else:
                    self.head = node 
                return 
            previous_node = current_node 
            current_node = current_node.next
if __name__ == "__main__":
    ll = LinkedList() 
    ll.append(2) 
    ll.append(3)
    ll.prepend(5)
    ll.show()
    print(ll.find(10))
    ll.delete(2)
    ll.show()
    ll.delete(5) 
    ll.show()
    ll.insert_before(3,10)
    ll.show()