class Node:
    def __init__(self , data) -> None:
        self.data = data 
        self.previous = None 

class Queue:
    def __init__(self) -> None:
        self.front = None 
        self.back = None 
    
    def enqueue(self , value):
        node = Node(value)
        if self.front is None:
            self.front = node 
        else:
            self.back.previous = node 
        
        self.back = node 

    def dequeue(self):
        if self.front is None : return 

        node = self.front 
        self.front = self.front.previous
        if self.front is None:
            self.back = None 
        
        return node.data  

    def print(self):
        current = self.front 

        while current :
            print(current.data)
            current = current.previous 
        
    
if __name__ == "__main__":
    queue = Queue() 
    queue.enqueue(2) 
    queue.enqueue(5) 
    queue.enqueue(6) 
    queue.print() 
    front = queue.dequeue() 
    print(front)
    print("After Dequeing") 

    queue.print()