import matplotlib.pyplot as plt
import graph as g 


def gen_all_edges (num_nodes):

    lst_tups = []
    for x in range (num_nodes):
        for  y in range (x , num_nodes):
            lst_tups.append((x,y))
    return lst_tups



def run_tests(epochs, num_nodes, tot_edges, lst_tups  ,label):
    probs     = []
    for num_edges in range (tot_edges):
        num_cycs = 0
        for _ in range(epochs):
            graph = g.create_rand_graph_safe_fast(num_nodes,num_edges,lst_tups.copy())
            if g.has_cycle(graph):
                num_cycs += 1
                #print(graph.adj)
             #print (num_cycs)
        probs.append(num_cycs/epochs)
    plt.plot(probs, label=label)


epochs    = 10000
num_nodes_1 = 100
num_nodes_2 = 90
num_nodes_3 = 80



run_tests(epochs,num_nodes_1, num_nodes_1 -1 , gen_all_edges(num_nodes_1) ,"size: 100")
run_tests(epochs,num_nodes_2, num_nodes_2 -1 , gen_all_edges(num_nodes_2) ,"size: 90")
run_tests(epochs,num_nodes_3, num_nodes_3 -1 , gen_all_edges(num_nodes_3) ,"size: 80")

plt.legend(loc="upper left")
plt.title("Edge vs Cycle Probability")
plt.xlabel("Number of edges")
plt.ylabel("Cycle Probability")
plt.show()
    


