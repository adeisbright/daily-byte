'''
A tree data structure is used for storing hierachical data. 
It consists of a root node with children nodes. 
The height of the tree is the path that returns the 
longest edges (edge count) 

For a binary tree, each node can have a maximum of two children. 


'''
class BinaryNode :
    def __init__(self ,data):
        self.data = data 
        self.left = None 
        self.right = None 
    


class BinaryTree:
    def __init__(self) -> None:
        self.root = None 
    
    def insert(self , data):
        if self.root is None:
            self.root = BinaryNode(data)
        else:
            self._insert_helper(self.root , data)
    
    def _insert_helper(self , node , data):
        if data < node.data :
            if node.left is None :
                node.left = BinaryNode(data)
            else:
                self._insert_helper(node.left , data)
        else:
            if node.right is None :
                node.right = BinaryNode(data)
            else:
                self._insert_helper(node.right , data)

    def traverse(self):
        self._traverse_helper(self.root)
    
    def _traverse_helper(self , node):
        if node is not None:
            self._traverse_helper(node.left)
            print(node.data) 
            self._traverse_helper(node.right)

    
if __name__ == "__main__":
    
   # Create the binary tree
    tree = BinaryTree()

    # Insert nodes into the binary tree
    tree.insert(5)
    tree.insert(3)
    tree.insert(8)
    tree.insert(2)
    tree.insert(4)
    tree.insert(7)
    tree.insert(9)

    # Traverse the binary tree in inorder
    tree.traverse()
