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

        if node1 == node2:
            self.adj[node1].append(node2)
            return


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
                path_pred[node ] = current_node 
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
            #print(G.adj[current_node])
            for node in G.adj[current_node]:
                if not marked[node]:
                    pred[node] = current_node 
                S.append(node)
            #print(pred)
    return pred


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
    S = [node1]
    marked = {}
    parents = []
    grandp  = []
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop() 
        if not marked[current_node]:
            print ("__________________")
            print ("cur  GP" , grandp)
            print("curs parents:", parents)
            print("cur node", current_node)
            grandp += parents
            marked[current_node] = True
            parents.append(current_node)
            for node in G.adj[current_node]:
                if node in grandp  and not marked[node]:
                    print ("end cur",  node )
                    print ("end cur  GP" , grandp)
                    print("end curs parents:", parents)
                    return True
                S.append(node)
                prevnode = current_node
            print ("__________________")

        #print("Current depth: " , depth)

    #print("END DEPTH", depth)

    lstnode = [k  for k in marked if marked[k] ]
    return False
   
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

def has_cyclePrint (G: Graph):
    for node in G.adj:
        print (isCycle(G,node))
        
    return False

def has_cycle (G: Graph):
    for node in G.adj:
        if isCycle(G,node):
            return True
        
    return False
test = Graph(7)

test.add_edge(0,1)
test.add_edge(0,6)
test.add_edge(1,2)
test.add_edge(2,4)
test.add_edge(4,0)
test.add_edge(2,5)

#test.add_edge(1,3)
#test.add_edge(2,4)
#test.add_edge(2,3)
#test.add_edge(3,4)
#test.add_edge(3,5)
print(test)
print (BFS3(test,0))
print(DFS3(test,0))

def create_full_graph (num_nodes):
    lst_tups = []
    G = Graph(num_nodes)
    for x in range (num_nodes):
        for  y in range (x , num_nodes):
            G.add_edge(x,y)
    return G

def create_rand_graph_safe (num_nodes, num_edges):
    lst_tups = []
    G = Graph(num_nodes)
    for x in range (num_nodes):
        for  y in range (x , num_nodes):
            lst_tups.append((x,y))
    for i  in range (num_edges):
        tup = lst_tups.pop(random.randint(0, len(lst_tups) - 1))
        x = tup[0]
        y = tup[1]
        G.add_edge(x,y)
    return G

g=  create_rand_graph_safe(1000,1000)
create_full_graph(5)
print (g.adj)
