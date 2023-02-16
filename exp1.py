import matplotlib.pyplot as plt
import graph as g 
from tqdm import tqdm



def run_tests(epochs, num_nodes, tot_edges, label):
    probs     = []
    # note u should delete the tqdm package
    for num_edges in  tqdm(range (tot_edges)):
        num_cycs = 0
        for _ in range(epochs):
            graph = g.create_rand_graph_safe(num_nodes,num_edges)
            if g.has_cycle(graph):
                num_cycs += 1
                #print(graph.adj)
             #print (num_cycs)
        probs.append(num_cycs/epochs)
    plt.plot(probs, label=label)


epochs    = 1000
num_nodes_1 = 100
num_nodes_2 = 90
num_nodes_3 = 80

run_tests(epochs,num_nodes_1, num_nodes_1 -1 , "size: 100")
run_tests(epochs,num_nodes_2, num_nodes_2 -1 , "size: 90")
run_tests(epochs,num_nodes_3, num_nodes_3 -1 , "size: 80")

plt.legend(loc="upper left")
plt.title("Edge vs Cycle Probability")
plt.xlabel("Number of edges")
plt.ylabel("Cycle Probability")
plt.show()
    


