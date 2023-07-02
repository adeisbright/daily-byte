'''
A tree data structure is used for storing hierachical data. 
It consists of a root node with children nodes. 
The height of the tree is the path that returns the 
longest edges (edge count) 

For a binary tree, each node can have a maximum of two children. 


'''
class Node :
    def __init__(self , value , left=None , right=None):
        self.value = value 
        self.left = left 
        self.right = right 
    


class BinaryTree:
    def __init__(self) -> None:
        self.root = None 
    
    def add_node(self,data):
        return self.root
