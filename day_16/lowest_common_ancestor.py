'''
Given a binary search tree that contains unique values
 and two nodes within the tree, a, and b, return their 
 lowest common ancestor.
Note: the lowest common ancestor of two nodes
 is the deepest node within the tree such that both nodes are descendants of it.

Ex: Given the following tree...
       7
      / \
    2    9
   / \ 
  1   5 
and a = 1, b = 9, return a reference to the node containing 7.
Ex: Given the following tree...

        8
       / \
      3   9
     / \ 
    2   6
and a = 2, b = 6, return a reference to the node containing 3.
Ex: Given the following tree...

        8
       / \
      6   9
and a = 6, b = 8, return a reference to the node containing 8.
'''

'''
To solve this problem, I will follow this path :
-> Get the parent for each node that is provided, and store that parent in a set 
-> Now find the intersection of the parents 

I will need to write a function that takes provides the parents of a node .
Let us call this function get ancestors 
'''
ancestors = set()
class BinaryNode:
    def __init__(self,data) -> None:
        self.data = data  
        self.left = None 
        self.right = None 
    

class Tree:
    def __init__(self) -> None:
        self.root = None 

    def add_node(self , data) :
        if self.root is None:
            self.root = BinaryNode(data)
        else:
            return self._add_node_helper(self.root , data)

    def _add_node_helper(self,node , data):
        if data < node.data:
            if node.left is None:
                node.left = BinaryNode(data)
            else:
                return self._add_node_helper(node.left , data)
        else:
            if node.right is None:
                node.right = BinaryNode(data)
            else:
                return self._add_node_helper(node.right , data)
    
    def get_ancestors(self , data):
        return self._get_ancestor_helper(self.root , data)
    
    def _get_ancestor_helper(self, node , data):
        

        if node.data == data : 
            ancestors.add(node.data)
            return ancestors
        if data < node.data:
            ancestors.add(node.data)
            if node.left is not None: 
                if node.left.data == data : 
                    return ancestors
                else : 
                    return self._get_ancestor_helper(node.left , data)
        else:
            ancestors.add(node.data)
            if node.right is not None:
                if node.right.data == data : return ancestors
                else : return self._get_ancestor_helper(node.right , data) 
        
        return ancestors
    
if __name__ == "__main__":
    tree = Tree()
    tree.add_node(7) 
    tree.add_node(2) 
    tree.add_node(9) 
    tree.add_node(1) 
    tree.add_node(5) 
    tree.add_node(6) 
    tree.add_node(8) 
    
    test = tree.get_ancestors(2)
    

    print(test)