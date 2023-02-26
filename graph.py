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

    def number_of_nodes(self):
        return len(self.adj)

    def returnAdj(self):
        print(self.adj)


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


#Breadth First Search
def BFS2(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    
    path = [] #initalizing list of nodes needed to travel from node1 to node2 on the shortest path
    
    for node in G.adj:
        if node != node1: 
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        
        path.append(current_node) #adding to the list "path" the current node we are at
        for node in G.adj[current_node]:
            if node == node2:
                #adding to the list "path" the node that we are looking for, node2, and then printing the whole path from node1 to node2
                path.append(node)
                
                #printing a new list "answer" which will remove nodes from "path" that are not part of shortest path from node1 to node2
                answerKey = node                
                answer = [node]
                for i in range(len(path)-2, -1, -1):
                    if answerKey in G.adj[path[i]]:
                       answer.append(path[i])
                       answerKey = path[i]
                print(answer)            
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                path.append(node)  #adding to the "path" list the node that we have not visited before that may be part of final path
            else:
                #if we encounter a node that we already marked and does not help us find a path from node1 to node2,
                # then we delete that node from the "path" list
                path.pop()
    print([]) #print empty list if there is no path from node1 to node2
    return False

#Depth First Search
def DFS2(G, node1, node2):
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

def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(len(G.adj))]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover

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

#approx1
def approx1(G):
    C = set()
    copy = Graph(len(G.adj))
    for node in G.adj:
        for adjacent_node in G.adj[node]:
            copy.add_edge(node, adjacent_node)
    vertex_cover=False
    
    while vertex_cover == False:
        max_degree_node = None
        max_degree = -1
        for node in copy.adj:
            degree = len(copy.adjacent_nodes(node))
            if degree > max_degree:
                max_degree_node = node
                max_degree = degree
        v = max_degree_node
        print(v)
        C.add(v)
        for node in copy.adjacent_nodes(v):
            if (v in copy.adj[node]):
                copy.adj[node].remove(v)
        del copy.adj[v]
        if (is_vertex_cover(G, C)==True):
            vertex_cover=True
    return C

#approx2
def approx2(G):
    C = set()
    while not is_vertex_cover(G, C):
        v = random.choice([node for node in G.adj if node not in C])
        C.add(v)
    return C

#approx3
def approx3(G):
    C = set()
    copy = Graph(len(G.adj))
    for node in G.adj:
        for adjacent_node in G.adj[node]:
            copy.add_edge(node, adjacent_node)
    vertex_cover=False
    
    while vertex_cover==False:
        select = False
        while select == False:
            v = random.choice([node for node in G.adj])
            if (len(copy.adj[v])>=1):
                c = random.choice(copy.adj[v])
                select = True
        C.add(v)
        C.add(c)
        for node in copy.adjacent_nodes(v):
            if (v in copy.adj[node]):
                copy.adj[node].remove(v)
            if (c in copy.adj[node]):
                copy.adj[node].remove(c)
        if (is_vertex_cover(G, C)==True):
            vertex_cover=True
    return C

# Created random graph
def create_random_graph(i, j):
    G = Graph(i)
    for _ in range(j):
        rand1 = random.randint(0,i - 1)
        rand2 = random.randint(0,i - 1)    
        while ( rand2 in G.adj[rand1] ):
            print (rand1,rand2, "U may have added too many nodes")
            rand1 = random.randint(0,i - 1)
            rand2 = random.randint(0,i - 1) 
        
        G.add_edge (rand1, rand2)
    return G
# Created random graph
""" The problem with the create random
    function above is that it can potentially
    run into the while loop multiple tims. 
    This function is more safe then that version 
    beacuse it just crashes if too many edges 
    are added, and potentially faster since we 
    are not needlessly looping over nodes we already
    added.
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

# Created a faster version of the create_rand_graph_safe function
# now successive runs of this functions will not be as slow since
# we do need to calculte the lst_tups lst as often
def create_rand_graph_safe_fast (num_nodes, num_edges ,lst_tups):
    G = Graph(num_nodes)
    for i  in range (num_edges):
        if len(lst_tups) == 0 :
            print ("You added to many edges.")
        tup = lst_tups.pop(random.randint(0, len(lst_tups) - 1))
        x = tup[0]
        y = tup[1]
        G.add_edge(x,y)
    return G

if __name__ == "__main__":
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
