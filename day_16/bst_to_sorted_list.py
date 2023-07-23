'''
Given a binary search tree, rearrange the tree such that
it forms a linked list where all its values 
are in ascending order.

Ex: Given the following tree...
        5
       / \
      1   6
return...

1
 \
  5
   \
    6
Ex: Given the following tree...

       5
      / \
    2    9
   / \ 
  1   3 
return...

1
 \
  2
   \
    3
     \
      5
       \
        9
Ex: Given the following tree...

5
 \
  6
return...

5
 \
  6

'''

import sys 
from os import path 
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from day_15.find_tree_node import BST 
from day_7.linked_list import LinkedList 

class BSTLinkedList(BST):
    def __init__(self):
        super().__init__()
        self.l  = LinkedList()

    def traverse_and_append(self):
        self._traverse_helper(self.root)

    def _traverse_helper(self , node):
        if node is not None:
            self._traverse_helper(node.left)
            self.l.append(node.data)
            self._traverse_helper(node.right)
    def show_list(self):
        return self.l.show()

if __name__ == "__main__":
    tree = BSTLinkedList() 
    tree.add_node(5) 
    tree.add_node(2) 
    tree.add_node(9) 
    tree.add_node(1) 
    tree.add_node(3) 
    
    tree.traverse_and_append() 

    tree.show_list()
