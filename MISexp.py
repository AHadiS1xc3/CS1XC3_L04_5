
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

def is_A_Cover (lst_verts, G:g.Graph):
	"""	
	pos_edges = [ ]
	for x in range (len(lst_verts)):
		for y in range (x,len(lst_verts)):
			pos_edges.append ((lst_verts[x],lst_verts[y]))

	"""
	edges_in_g = []
	for e1 in list(G.adj.keys()):
		for e2 in G.adj[e1]:
			edges_in_g.append((e1,e2))

	for (e1,e2) in edges_in_g :
		if  e1 not in lst_verts and e2 not in lst_verts:
			return False  


	return True

def MVC(G:g.Graph):
	power_set_verts = powerSetVert(list(G.adj))

	min_vert = list(G.adj.keys())
	for verts in power_set_verts:
		if is_A_Cover (verts,G):
            #print(verts)
			if len(verts) < len (min_vert):
				min_vert = verts
	return min_vert


l = [1,2,3]


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
print(MVC(graph1))
#print(powerSetVert([1,2,3,4]))






