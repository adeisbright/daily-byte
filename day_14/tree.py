class BinaryNode:
    def __init__(self , data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

i = 0
class BinaryTree :
    def __init__(self) -> None:
        self.root = None 
        self.length = 0 
        self.i = 0
    def add_node(self , data):
        if self.root is None:
            self.root = BinaryNode(data) 
        else:
            self._add_node_helper(self.root , data) 
    
    def _add_node_helper(self , node , data):
        if data < node.data :
            if node.left is None:
                node.left = BinaryNode(data) 
            else:
                self._add_node_helper(node.left,data) 
        else:
            if node.right is None:
                node.right = BinaryNode(data)
            else:
                self._add_node_helper(node.right , data)
    def _tranver_helper(self , node):
        if  node is not None:
            self._tranver_helper(node.left)
            print(node.data)
            self._tranver_helper(node.right)
            
           
    def traverse(self):
        self._tranver_helper(self.root)

    def find_helper(self , node , value):
       
        if node is None: return False 
        if node is not None and node.data == value : return True 
        if value < node.data:
            if node.left is not None: 
                if value == node.left.data:
                    return True 
                else:
                    return self.find_helper(node.left,value) 
            else:
                return False 
        else:
            if node.right is not None:
                if value == node.right.data :

                    return True 
                else:
                    return self.find_helper(node.right , value)
            else:
                return False
    def find(self , value): 
        return self.find_helper(self.root , value)

    def find_successor(self , node):
        current = node 
      
        while current.left is not None:
           
            current = current.left 
        return current 
    
    def delete(self,root , value):
        #Find and confirm if the node exists 
        if root is None:
            return root 
        
        #Search for the node to be deleted 
        if value < root.data:
            root.left = self.delete(root.left , value) 
        elif value > root.data:
            root.right = self.delete(root.right , value) 
        else:
            if root.left is None:
                temp = root.right
                root = None 
                return temp 
            elif root.right is None:
                temp = root.left 
                root = None 
                return temp 
            temp = self.find_successor(root.right) 
            root.data = temp.data 
            root.right = self.delete(root.right , temp.data)

        return root 


test = BinaryTree()

test.add_node(5) 
test.add_node(3) 
test.add_node(4) 
test.add_node(6) 
test.add_node(2) 
test.traverse()

test.delete(test.root , 3) 
print("Now Traversing after delete")
test.traverse()
# b = test.find(2) 
# print(b)