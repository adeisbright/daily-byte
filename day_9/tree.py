class Node:
    def __init__(self , data) -> None:
        self.data = data 
        self.children = []

    def add_child(self , child):
        try:
            if not isinstance(child , Node):
                raise Exception("Issues")
            
            self.children.append(child)
        except Exception as error:
            print(error)


class Tree:
    def __init__(self , root) -> None:
        self.root = root 
    
    def traverse(self):
        return self._traverse_helper(self.root)
    
    def _traverse_helper(self , node):
        print(node.data)
        for node in node.children:
            self._traverse_helper(node)



if __name__ == "__main__":
    
    # Create nodes
    root_node = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_d = Node('D')
    node_e = Node('E')

    # Build the tree structure
    root_node.add_child(node_b)
    root_node.add_child(node_c)
    node_b.add_child(node_d)
    node_b.add_child(node_e)

    # Create the tree
    tree = Tree(root_node)

    # Traverse the tree and print the node data
    tree.traverse()
 