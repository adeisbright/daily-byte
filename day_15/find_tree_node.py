'''
Given the reference to the root of a binary search tree and a search value,
return the reference to the node that contains the value 
if it exists and null otherwise.
Note: all values in the binary search tree will be unique.

Ex: Given the tree...

        3
       / \
      1   4
and the search value 1 return a reference to the node containing 1.
Ex: Given the following tree...

        7
       / \
      5   9
         / \ 
        8   10
and the search value 9 return a reference to the node containing 9.
Ex: Given the following tree...

        8
       / \
      6   9
and the search value 7 return null.
'''

class BinaryNode:
    def __init__(self , data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 


class BST:
    def __init__(self) -> None:
        self.root = None 
    
    def add_node(self , value):
        if self.root is None:
            self.root = BinaryNode(value) 
        else:
            return self._add_node_helper(self.root , value)
        
    def _add_node_helper(self , node , value):
        if value < node.data:
            if node.left is None:
                node.left = BinaryNode(value) 
            else:
                return self._add_node_helper(node.left , value)
        else:
            if node.right is None:
                node.right = BinaryNode(value)
            else:
                return self._add_node_helper(node.right , value)
                
    def find(self , value):
        return self._find_helper(self.root , value) 
    
    def _find_helper(self , node , value):
        if node is None: return None 
        if node.data == value : return node.data 

        if value < node.data:
            if node.left is None: return None 
            if value == node.left.data: return node.left.data 
            else: return self._find_helper(node.left , value)
        else:
            if node.right is None : return False 
            if node.data == value: return node.data 
            else : return self._find_helper(node.right , value)


if __name__ == "__main__":
    tree = BST() 
    tree.add_node(10) 
    tree.add_node(8) 
    tree.add_node(11) 
    test = tree.find(8)  
    print(test)
    