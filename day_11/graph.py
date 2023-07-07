'''
/**
 * A graph is a data structure with finite nodes(called vertices)
 * and edges 
 * 
 * A Graph is denoted as G(V , E) , read as G is a Set of 
 * V(Vertices) , and E(Edges) 
 * 
 * The nodes are stationed points on the graph while the edges 
 * are the lines connecting one point to another 
 * 
 * Termilogies related to graphs 
 * Nodes 
 * Edges 
 * Cycle 
 * Degree 
 * Traversal 
 * Path
 * 
 * A trivial graph is a graph with only one node and no 
 * edges
 * 
 * A single graph is a graph where the number of edges between 
 * any node is one.
 * The opposite of simple graph is multi-graph.
 * 
 * A null graph is a graph without edges but nodes 
 * 
 * A graph is complete if all nodes are connected to one another
 * 
 * A pseudo-graph has atleast one node with a self connected 
 * edge.
 * 
 * A graph can be directed or un-directed 
 * 
 * A directed grah is a graph whose nodes are connected  to one
 * another with directions
 * 
 * An Undirected graph has nodes that are not connected  to one 
 * another
 * 
 * A regular graph is a graph where each node has the same 
 * amount of degree meaning the same number of edges connected 
 * to each node
 * 
 * A weighted graph is a graph where edges possess a weight 
 * showing the cost of tranversal from one point 
 * to the other.
 * 
 * A cyclic graph has atleast one cycle. You can traverse from 
 * a point to all nodes.
 * The opposite is acyclic
 * 
 * Graph Representation
 * -------------------- 
 * A graph can be represented using :
 * Adjancency List 
 * Adjancency Matrix  
 * 
 * Nodes    A   B   C   D
 * A        0   1   0   0
 * B        0   0   1   0
 * C        0   0   0   1
 * D        1   0   0   0
 * 
 * 
 * 
 * Graph Tranversal
 * Graph tranversal refers to going through each node once.
 * 
 * You can go through a graph  using two methods :
 * > Breadth First Search Algorithm 
 * Starts tranversing the graph by starting from the root 
 * node and explore all the neighbouring nodes.
 * Then move to the next node and do the same 
 * 
 * A Queue is used for BFS 
 * 
 * > Depth First Search Algorithm
 * Start from the initial node of the graph and go deeper 
 * till you find a graph that has no child. 
 * 
 * Then move to an unexplored node.
 * A stack is used for DFS 
 */

 
'''
import sys 
from os import path 
sys.path.append(path.dirname(path.dirname(path.abspath(__file__)))) 

from day_8.queue import Queue 

class Graph:
    ''' This graph implementation uses an undirected graph '''
    def __init__(self):

        self.vertex = {}

    def add_vertex(self , data):
        if data not in self.vertex:
            self.vertex[data] = []
    
    def add_edge(self , node1 , node2):
        try:
            if self.vertex.get(node1) is None or self.vertex.get(node2) is None:
                raise Exception("You have a non-existent node")
            first_edge_count = self.vertex[node1].count(node2)  
            second_edge_count = self.vertex[node2].count(node1) 

            if  first_edge_count != 0 or  second_edge_count != 0 :
                raise Exception("Edge already exist between {node1} and {node2}".format(node1=node1 , node2=node2))
            
            self.vertex[node1].append(node2) 
            self.vertex[node2].append(node1)
        except Exception as error:
            print(error)

    
    def print_graph(self):
        vertices = self.vertex.keys() 
        for vertex in vertices:
            edges = self.vertex.get(vertex) 
          
            linear_edges = "" 
            for edge in edges:
                linear_edges += str(edge) + " "

            print(str(vertex) + " -> "  , linear_edges)
            # Get all the edges 

    def bfs(self , starting_vertex):
        visited = set() 

        queue = Queue() 
        queue.enqueue(starting_vertex) 
     
       
      
        while queue:
            vertex = queue.dequeue() 
           
            if vertex and vertex not in visited:
                visited.add(vertex) 
                print("vertex ->" , vertex)
            if vertex:
                neighbors = self.vertex[vertex] 

                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.enqueue(neighbor) 
if __name__ == "__main__":

    g = Graph() 
    g.add_vertex(2) 
    g.add_vertex(2) 
    g.add_vertex(3)
    g.add_vertex(1) 
    g.add_edge(2 , 3)
    g.add_edge(1 , 2)
    g.add_edge(1 , 2)

    g.print_graph() 

    g.bfs(2)