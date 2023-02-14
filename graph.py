from collections import deque
import random
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

    def number_of_nodes():
        return len()


#Breadth First Search
def BFS(G : Graph, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False




#Depth First Search
def DFS(G : Graph, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False


def BFS3 (G: Graph , node1: int  ):
    path_pred = {}
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                path_pred[node] = current_node 
                Q.append(node)
                marked[node] = True
    return path_pred


#DFS3
def DFS3(G : Graph, node1):
    S = [node1]
    pred = {}
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if not marked[node]:
                    pred[node] = current_node 
                S.append(node)
    return pred

#has_cycle
def has_cycle(G):
    def DFSCycleChecker(node1, parent, marked):
        marked[node1] = True
        for node in G.adjacent_nodes(node1):
            if marked[node] == False:
                if DFSCycleChecker(node, node1, marked) == True:
                    return True
            elif node != parent:
                return True
        return False
    marked = [False] * len(G.adj)
    for i in range(len(G.adj)):
        if marked[i] == False:
            if DFSCycleChecker(i, -1, marked) == True:
                return True
    return False

#is_connected
def is_connected(G):
    def dfs(node, marked):
        marked.add(node)
        for adj in G.adjacent_nodes(node):
            if adj not in marked:
                dfs(adj, marked)

    marked = set()
    dfs(list(G.adj.keys())[0], marked)
    return len(marked) == len(G.adj)

# Created random graph
def create_random_graph(i, j):
    G = Graph(i)
    for _ in range(j):
        rand1 = random.randint(0,i - 1)
        rand2 = random.randint(0,i - 1)    
        while ( rand2 in G.adj[rand1]):
            print (rand1,rand2)
            rand1 = random.randint(0,i - 1)
            rand2 = random.randint(0,i - 1)    
        G.add_edge (rand1, rand2)
    return G
# Created random graph
""" The problem with the create random
    function above is that it can potentially
    run into an infinite while loop. 
    This function is more safe then that version 
    beacuse it just crashes if too many edges 
    are added
"""
def create_rand_graph_safe (num_nodes, num_edges):
    lst_tups = []
    G = Graph(num_nodes)
    for x in range (num_nodes):
        for  y in range (x , num_nodes):
            lst_tups.append((x,y))
    for i  in range (num_edges):

        if len(lst_tups) == 0 :
            print ("You added to many edges.")
        tup = lst_tups.pop(random.randint(0, len(lst_tups) - 1))
        x = tup[0]
        y = tup[1]
        G.add_edge(x,y)
    return G

if __name__ == "main":
    test = Graph(6)

    test.add_edge(0,1)
    test.add_edge(1,2)
    test.add_edge(2,4)
    test.add_edge(4,0)

    #test.add_edge(1,3)
    #test.add_edge(2,4)
    #test.add_edge(2,3)
    #test.add_edge(3,4)
    #test.add_edge(3,5)
    print(test)
    print (BFS3(test,0))
    print(DFS3(test,0))
    print((has_cycle(test)))
