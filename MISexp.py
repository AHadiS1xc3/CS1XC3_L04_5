import graph as g
import matplotlib.pyplot as plt

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

def subTract (L1, L2):
	L3 = []
	for x in L1:
		if x not in L2:
			L3.append(x)

	return L3





def MIS(G:g.Graph):
	tot      = list(G.adj.keys())
	#power_set = powerSetVert(list(G.adj))
	power_set_verts = powerSetVert(list(G.adj))

	"""	for lst in power_set:
		power_set_verts.append(lst)"""
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


def run_size_sum_test(num_nodes, num_runs):
	sum_size = []
	for num_edges in range (num_runs):
		graph = g.create_rand_graph_safe(num_nodes,num_edges)
		sum_lst = len (MIS(graph)) + len(MVC(graph))
		sum_size.append(sum_lst)
	plt.plot(sum_size, label="Graph with " + str(num_nodes) + " nodes" )

def is_A_Mvc (lst_verts, G:g.Graph):
	return is_A_Cover(lst_verts, G) and len(lst_verts) == len(MVC(G))

def run_complement_tests (num_nodes, num_runs):
	graph = g.create_rand_graph_safe(num_nodes,0)
	num_adj = len (str(list(graph.adj.keys())))

	string = "Graph verts".ljust(num_adj, " ")
	string+= " | "
	string+= "MIS".ljust(num_adj," ")
	string+= " | "
	string+= "Potentail MVC".ljust(num_adj," ")
	string+= " | "
	string+= "IS AN MVC?\n" 


	for num_edges in range (num_runs):
		graph = g.create_rand_graph_safe(num_nodes,num_edges)
		num_adj = len (str(list(graph.adj.keys())))
		mis = MIS(graph)
		lst_graph_verts = list(graph.adj.keys())
		potentail_MVC = subTract(lst_graph_verts, mis )
		fax = is_A_Mvc(potentail_MVC,graph)
		string+= str(lst_graph_verts) + " - " + str(mis).ljust(num_adj , " ") + " = " + str( potentail_MVC ).ljust(num_adj , " ")  + "  " + str(fax) + "\n"

	print(string)
		
	pass


run1 = True
run2 = True
#--- CODE BELOW GENERATED FIG IV.1 ----
if run1:
	run_size_sum_test(10,20)
	run_size_sum_test(11,20)
	run_size_sum_test(12,20)
	run_size_sum_test(13,20)
	plt.title("Number of edges vs Sum Size")
	plt.ylabel("Sum Size")
	plt.xlabel("Number of edges")
	plt.legend(loc="upper left" , bbox_to_anchor=(1,0.5))
	plt.show()
#-------------------------------------


if run2:
	#--- CODE BELOW GENERATED FIG IVCT.1 ----
	run_complement_tests(10,20)
	#----------------------------------------

	#--- CODE BELOW GENERATED FIG IVCT.2 ----
	run_complement_tests(11,20)
	#----------------------------------------

	#--- CODE BELOW GENERATED FIG IVCT.3 ----
	run_complement_tests(12,20)
	#----------------------------------------

	#--- CODE BELOW GENERATED FIG IVCT.4 ----
	run_complement_tests(13,20)
	#----------------------------------------
	

#print(powerSetVert([1,2,3,4]))
