from queuer import Queue
from collections import deque
class Graph:
    def __init__(self) -> None:
        self.vertex = {} 

    
    def add_vertice(self , data):
        if data not in self.vertex:
            self.vertex[data] = [] 
        
    def add_edge(self , node1 , node2):
        try:
            if node1 not in self.vertex or node2 not in self.vertex:
                raise Exception("One of your node is not created yet") 
            
            first_edge_count = self.vertex[node1].count(node2) 
            second_edge_count = self.vertex[node1].count(node2)  

            if first_edge_count != 0 or second_edge_count != 0 :
                raise Exception("Edges already exists between the nodes {} {}".format(node1 , node2)) 
            
            self.vertex[node1].append(node2) 
            self.vertex[node2].append(node1)
        except Exception as error:
            print(error)

    def print(self):
        vertices = self.vertex.keys() 

        for key in vertices:
            print(key ,"->" ,  self.vertex[key]) 
        
    def bfs(self , starting_vertex):
        visited = set()

        # queue = deque([starting_vertex]) 
        queue = Queue() 
        queue.enqueue(starting_vertex)

        while queue.front:
            vertex = queue.dequeue()
            # vertex = queue.popleft()

            if vertex and vertex not in visited:
                visited.add(vertex)
                print(vertex)
                neighbors = self.vertex[vertex] 
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.enqueue(neighbor)
                        # queue.append(neighbor)
    
    def shortest_distance(self , a , b) :
        
        if a not in self.vertex or b not in self.vertex : return -1 
        visited = set() 
        queue = deque([(a , 0)])

        while queue:
            node , distance = queue.popleft()
            print("distance is " , distance)
            visited.add(node)
            if node == b :
                return distance 
                
            for neighbor in self.vertex[node]:
                if neighbor not in visited:
                    queue.append((neighbor , distance + 1))
        return -1 

    def dfs(self, start_vertex):
        visited = set()

        def dfs_helper(vertex):
            visited.add(vertex)
            print(vertex, end=' ')

            if vertex in self.vertex:
                for neighbor in self.vertex[vertex]:
                    if neighbor not in visited:
                        dfs_helper(neighbor)

        dfs_helper(start_vertex)  

if __name__ == "__main__":
    graph = Graph() 

    graph.add_vertice("A") 
    graph.add_vertice("B") 
    graph.add_vertice("C") 
    graph.add_vertice("D") 
    graph.add_vertice("E") 
    graph.add_vertice("F") 

    graph.add_edge("A" , "B") 
    graph.add_edge("A" , "C") 
    graph.add_edge("B" , "D") 
    graph.add_edge("B" , "F") 
    graph.add_edge("C" , "E") 
    graph.add_edge("D" , "E") 
    graph.add_edge("D" , "F") 
    graph.add_edge("E" , "F") 
 
    test = graph.shortest_distance("A" , "F") 
    print(test)
