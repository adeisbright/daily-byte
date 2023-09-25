# Re-learning Tree 

class TreeNode:
    def __init__(self , data):
        self.data =  data 
        self.left = None 
        self.right = None 



class BST:
    def __init__(self) :
        self.root = None 

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_helper(self.root , value)
    def _insert_helper(self,node , data ):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data) 
            else:
                self._insert_helper(node.left , data) 
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_helper(node.right , data) 

    def traverse(self):
        return self._traverse_helper(self.root)

    def _traverse_helper(self , node):
        if node is not None:
            self._traverse_helper(node.left) 
            print(node.data)
            self._traverse_helper(node.rigth)


