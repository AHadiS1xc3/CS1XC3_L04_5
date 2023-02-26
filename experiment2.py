from collections import deque
import random
import matplotlib.pyplot as plot

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)

    def returnAdj(self):
        print(self.adj)


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    path = []
    
    for node in G.adj:
        marked[node] = False
    
    while len(S) != 0:
        current_node = S.pop()
                
        if not marked[current_node]:

            #adding to the list "path" the current node we are at that is also not been visited before
            path.append(current_node)
            
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    #adding to the list "path" the node that we are looking for, node2, and then printing the whole path from node1 to node2
                    path.append(node)
                    print(path)
                    return True
                
                S.append(node)
        else:
            #if we encounter a node that we already marked and does not help us find a path from node1 to node2,
                # then we delete that node from the "path" list
            if len(path) > 0:
                path.pop()   
    
    #if we encounter no path from node1 to node2, then we print the empty list
    print([])
    return False

def create_random_graph(nodes, edges):
    G = Graph(nodes)
        
    nodes = [i for i in range(G.number_of_nodes())]
    
    edgeCount = 0
    while edgeCount < edges:
        node1 = random.randint(0,len(nodes)-1)
        node2 = random.randint(0,len(nodes)-1)
        
        if (not G.are_connected(node1, node2)) and node1 != node2:
            G.add_edge(node1, node2)
            edgeCount += 1
    
    return G


def is_Connected(G):
    
    nodes = [i for i in range(G.number_of_nodes())]
    
    for i in range(len(nodes)-1):
        if not DFS(G, nodes[i], nodes[i+1]):
            return False
    
    return True

def experiment(nodes, edges, graphs):    
    
    mGraphs = [create_random_graph(nodes, edges) for j in range(graphs)]
        
    isConnectedFacts = [is_Connected(k) for k in mGraphs]
    
    totalTrue = isConnectedFacts.count(True)
    
    return totalTrue / len(isConnectedFacts)
        
results = []
for i in range(0, 100):
    results.append(experiment(20, i, 100))
plot.plot(results)
plot.title("Probability of connected Graphs per number of edges")
plot.xlabel("Number of Edges for the graph")
plot.ylabel("Probability of Connectedness")
plot.show()
