class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 


class Queue :
    def __init__(self):
        self.front = None 
        self.back = None 
        self.size = 0 

    def enqueue(self,value):
        node = Node(value)
        if self.front is None:
            self.front = node 
        else:
            self.back.next = node 

        self.back  = node  
        self.size += 1

    def dequeue(self): 
        if self.front is None: return 
        
        node = self.front 
        self.front = self.front.next
       
        self.size -= 1
        return node.value 

    def peek(self):
        if self.front is None:
            return None 
        return self.front.value  
    
    def length(self):
        return self.size  
    
    def show(self):
        current_front = self.front 

        members = ''
        while current_front :

            members += "{value}->".format(value=current_front.value)

            current_front = current_front.next 
        print(members)


if __name__ == "__main__":
    q = Queue() 

    top = q.peek() 
    size = q.length() 
    print("The value at the top is {} and queue size is {}".format(top , size))
   
    q.enqueue(10) 
    q.enqueue(4)
    q.enqueue(9)
    q.enqueue(3)
    top = q.peek() 
    size = q.length() 
    print("The value at the top is {} and queue size is {}".format(top , size))
    q.show()
    q.dequeue() 
    q.show()
    q.dequeue() 
    q.show()

    q1 = Queue() 
    q1.enqueue(10)
    t = q1.dequeue() 
    print(t)
    

        