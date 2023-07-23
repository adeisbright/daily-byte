'''
Given an array of numbers sorted in ascending order, 
return a height-balanced binary search tree using every number from the array.
Note: height-balanced meaning that the level of any nodes 
two subtrees should not differ by more than one.

Ex: Given the following nums...

nums = [1, 2, 3] return a reference to the following tree...
       2
      /  \
     1    3
Ex: Given the following nums...

nums = [1, 2, 3, 4, 5, 6] return a reference to the following tree...
        3
       / \
      2   5
     /   / \
    1   4   6
'''

class TreeNode:
    def __init__(self , data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

    
# Let us create an helper function to create node 

def array_to_bst(nums):
    if not nums : return None 

    mid = len(nums)//2 
    root = TreeNode(nums[mid])

    root.left = array_to_bst(nums[:mid]) 
    root.right = array_to_bst(nums[mid + 1 : ])

    return root 

def inorder_traveral(root):
    if root is not None:
        inorder_traveral(root.left) 
        print(root.data) 
        inorder_traveral(root.right) 

def find_common_ancestor(root , a , b):
    return ca_helper(root , a , b)

def ca_helper(root , a , b):

    if root is None : return None 
    if a < root.data and b < root.data :
        return ca_helper(root.left , a , b)
    if a > root.data and b > root.data :
        return ca_helper(root.right , a , b) 
    return root.data 

if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bst = array_to_bst(sorted_array)
    # inorder_traveral(bst)
    test = find_common_ancestor(bst, 4 , 6 ) 
    print(test)