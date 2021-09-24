



class Node:
    def __init__(self, value = None):
        self.value = value
        
class Edge:
    def __init__(self, n1, n2, value = None):
        self.n1 = n1
        self.n2 - n2
        self.value = value
    
class Graph:
    def __init__(self, nodes = [], edges = []):
        
        
        for x,y in edges:
            if x not in nodes or y not in nodes:
                raise Exception("Nodes and edges are not consistent.")
        self.nodes = nodes
        self.edges = edges
        
    
    def add_node(self, node):
        """Adaugam un nod"""
        if node not in self.nodes:
            self.nodes.append(node)
        
    def add_edge(self, edge):
        """Adaugam o muchie"""
        #print(edge)
        if edge[0] not in self.nodes:
            self.add_node(edge[0])
        #print(edge)
        if edge[1] not in self.nodes:
            self.add_node(edge[1])
        #print(edge)
        if edge not in self.edges:
            self.edges.append(edge)
            
    def degree(self, node):
        """Get the degree of a graph"""
        if node not in nodes:
            raise Exception("This node is not in nodes list!")
        
        degree = 0
        for edge in self.edges:
            if node == edge[0]:
                degree+=1
        return degree
        
    def neighbours(self, node):
        neighbours = []
        for edge in self.edges:
            if node == edge[0]:
                neighbours.append(edge[1])
            
        return neighbours    
    
    def bfs(self, source):
        
        visited = set()
        visited.add(source)
        queue = []
        queue.append(0)
        res = []
        
        while queue:
            current_node = queue.pop(0)
            res.append(current_node)
            neigh_ = self.neighbours(current_node)
            for n in neigh_:
                if n not in visited:
                    queue.append(n)
                    visited.add(n)
        
        return res
    
    def _dfs(self, source, visited, res):
        
        res.append(source)
        
        neigh_ = self.neighbours(source)
        
        for n in neigh_:
            if n not in visited: 
                visited.add(n)
                self._dfs(n, visited, res)
        
    def dfs(self, source):
        visited = set()
        visited.add(source)
        res = []
        
        self._dfs(source, visited, res)
        
        return res
    
def graph_from_adjacency(matrix):
    ## Verificam daca matricea este patratica
    if len(matrix) != len(matrix[0]):
        raise Exception("Not a square matrix!")
    G = Graph()
    for i, row in enumerate(matrix):
        #print(row)
        for j, element in enumerate(row):
            
            if element == 1:
               # print((i,j))
                G.add_edge((i,j))
    return G
        
        
