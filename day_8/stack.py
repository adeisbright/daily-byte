class Node:
    def __init__(self,value) -> None:
        self.value = value 
        self.next = None 


class Stack :
    '''
    Implementing a Stack using a linked list.
    This implementation is because we are interested in operations 
    that runs in 0(1) 
    If we are interested in dynamic access and other list operations, we would 
    implement the stack using a list as the underlying data structure 
    
    '''
    def __init__(self) -> None:
        self.top = None 
        self.bottom  = None 
        self.size = 0 

    def push(self,value):
        node = Node(value)

        if self.bottom is None:
            self.bottom = node 
        else:
            node.next = self.top 

        self.top  = node  
        self.size += 1

    def pop(self):

        node = self.top 
        self.top = self.top.next
        self.size -= 1
        return node.value 

    def peek(self):
        if self.top is None:
            return None 
        return self.top.value  
    
    def length(self):
        return self.size  
    
    def show(self):
        current_top = self.top 

        members = ''
        while current_top :

            members += "{value}->".format(value=current_top.value)

            current_top = current_top.next 
        print(members)

    def stringnify(self):
        current_top = self.top 

        members = ''
        while current_top :

            members += "{value}".format(value=current_top.value)

            current_top = current_top.next 
        return members

if __name__ == "__main__":
    stack = Stack()
    stack.push(10) 
    stack.push(4) 
    stack.push(2) 

    stack.show() 

        