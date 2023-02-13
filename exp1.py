from collections import deque

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
                path_pred[node + 1] = current_node + 1
                Q.append(node)
                marked[node] = True
    return path_pred



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
            
            print(G.adj[current_node])
            for node in G.adj[current_node]:

                if not marked[node]:
                    pred[node +1] = current_node + 1
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


def paths (G:Graph, node1 ):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                S.append(node)
    lstnode = [k  for k in marked if marked[k] ]
    return lstnode

def isCycle (G:Graph , node1):
    
    p_node1 = paths(G,node1)

    for n1 in p_node1:
        for n2 in p_node1:
            if G.are_connected(n1,n2):
                return True
    return False


def has_cyclePrint (G: Graph):
    for node in G.adj:
        print(node,isCycle(G,node))
        
    return False


#test = Graph(6)

#test.add_edge(0,1)
#test.add_edge(1,2)
#test.add_edge(2,4)
#test.add_edge(4,0)

#test.add_edge(1,3)
#test.add_edge(2,4)
#test.add_edge(2,3)
#test.add_edge(3,4)
#test.add_edge(3,5)
#print(test)
#print (BFS3(test,0))
#print(DFS3(test,0))
#has_cyclePrint(test)
#print((has_cycle(test)))
