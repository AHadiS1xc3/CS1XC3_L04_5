import graph as g
import matplotlib.pyplot as plt
from tqdm import tqdm

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
	power_set = powerSetVert(list(G.adj))
	power_set_verts = []

	for lst in power_set:
		elm = subTract(tot,lst)

		power_set_verts.append(elm)
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
	for num_edges in tqdm(range (num_runs)):
		graph = g.create_rand_graph_safe(num_nodes,num_edges)
		sum_lst = len (MIS(graph)) + len(MVC(graph))
		sum_size.append(sum_lst)
	plt.plot(sum_size, label="Graph with " + str(num_nodes) + " nodes" )

def run_lst_sum_test(num_nodes, num_runs):

	graph = g.create_rand_graph_safe(num_nodes,0)
	num_adj = len (str(list(graph.adj.keys())))
	string = "MIS set".center(num_adj, " ")+ " | "
	string +="MVC set".center(num_adj, " ")+ " | "
	string +="Set concat".center(num_adj - 1," ")+ "| "
	string += "\n"
	string +="|".center(2*num_adj + 3 , "_") + "_"
	string +="|".ljust(num_adj,"_")+"_|"
	string += "\n"
	
	for num_edges in tqdm(range (num_runs)):
		graph = g.create_rand_graph_safe(num_nodes,num_edges)
		num_adj = len (str(list(graph.adj.keys())))
		mis     = MIS(graph)
		mvc     = MVC(graph)
		sum_lst = mis.copy() + mvc.copy()
		mis.sort()
		mvc.sort()
		sum_lst.sort()

		str_elm = " "*(3*num_adj+4) + " |\n"
		str_elm += str(mis).center(num_adj ," ")+" + " + str(mvc).center(num_adj, " ") + "="  + str(sum_lst) + " |\n"
		str_elm += "_"*(3*num_adj + 4) + "_|\n"
		string += str_elm

	print(string)

run1 = False
run2= True
if run1:
	run_size_sum_test(10,20)
	run_size_sum_test(11,20)
	run_size_sum_test(12,20)
	run_size_sum_test(13,20)
	plt.title("Number of edges vs Sum Size")
	plt.xlabel("Sum Size")
	plt.xlabel("Number of edges")
	plt.legend(loc="upper left" , bbox_to_anchor=(1,0.5))
	plt.show()

if run2:

	run_lst_sum_test(10,20)
	run_lst_sum_test(11,20)
	run_lst_sum_test(12,20)
	run_lst_sum_test(13,20)
	pass
#print(powerSetVert([1,2,3,4]))






