
import graph as g

def powerSetVert (lst_verts) :
    if len (lst_verts) == 0 :
        return [[]]
    else:
        

        oset =  powerSetVert(lst_verts[1:len(lst_verts)])
        pset =  []

        for lst in oset:
            elm = lst.copy()

            pset.append(elm)



        
        for lst in pset:
            lst.append(lst_verts[0])





        return oset +  pset


def isIndepSet (lst,G:g.Graph):

    pos_edges = [ ]


    for x in range (len(lst)):
        for y in range (x,len(lst)):
            pos_edges.append ((lst[x],lst[y]))

    
    #print("POS EDFGES: ", pos_edges)
    for edge in pos_edges:
        if G.are_connected(edge[0], edge[1]):
            return False
    
    
    return True
def MIS(G:g.Graph):
    power_set_verts = powerSetVert(list(G.adj))
    max_vert = []
    for verts in power_set_verts:
        if isIndepSet (verts,G):
            #print(verts)
            if len(verts) > len (max_vert):
                max_vert = verts
    return max_vert



graph1 = g.create_rand_graph_safe(5,5)

graph1 = g.Graph(8)


E = [ (1, 2),
      (1, 3),
      (2, 4),
      (5, 6),
      (6, 7),
      (4, 8)]

for (e1,e2) in E:
    graph1.add_edge(e1 - 1,e2 - 1)



print(graph1.adj)
print(graph1.adj.keys())
print(MIS(graph1))
#print(powerSetVert([1,2,3,4]))







# Python Program to implement
# the above approach

# Recursive Function to find the
# Maximal Independent Vertex Set
def graphSets(graph:g.Graph):
	
	# Base Case - Given Graph
	# has no nodes
	if(len(graph.adj) == 0):
		return []
	
	# Base Case - Given Graph
	# has 1 node
	if(len(graph.adj) == 1):
		return [list(graph.adj.keys())[0]]
	
	# Select a vertex from the graph
	vCurrent = list(graph.adj.keys())[0]
	
	# Case 1 - Proceed removing
	# the selected vertex
	# from the Maximal Set
	graph2 = graph
	
	# Delete current vertex
	# from the Graph
	del graph2.adj[vCurrent]
	
	# Recursive call - Gets
	# Maximal Set,
	# assuming current Vertex
	# not selected
	res1 = graphSets(graph2)
	
	# Case 2 - Proceed considering
	# the selected vertex as part
	# of the Maximal Set

	# Loop through its neighbours
	for v in graph.adj[vCurrent]:
		
		# Delete neighbor from
		# the current subgraph
		if(v in graph2.adj):
			del graph2.adj[v]
	
	# This result set contains VFirst,
	# and the result of recursive
	# call assuming neighbors of vFirst
	# are not selected
	res2 = [vCurrent] + graphSets(graph2)
	
	# Our final result is the one
	# which is bigger, return it
	if(len(res1) > len(res2)):
		return res1
	return res2

# Driver Code
V = 8

# Defines edges
E = [ (1, 2),
	(1, 3),
	(2, 4),
	(5, 6),
	(6, 7),
	(4, 8)]

graph = dict([])

# Constructs Graph as a dictionary
# of the following format-

# graph[VertexNumber V]
# = list[Neighbors of Vertex V]
for i in range(len(E)):
	v1, v2 = E[i]
	
	if(v1 not in graph):
		graph[v1] = []
	if(v2 not in graph):
		graph[v2] = []
	
	graph[v1].append(v2)
	graph[v2].append(v1)

# Recursive call considering
# all vertices in the maximum
# independent set
maximalIndependentSet = graphSets(graph1)

# Prints the Result
for i in maximalIndependentSet:
	print(i, end =" ")

