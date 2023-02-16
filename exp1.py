import matplotlib.pyplot as plt
import graph as g 
from tqdm import tqdm


epochs    = 10000
num_nodes = 10
num_runs  = 10*11//2

probs     = []
# note u should delete the tqdm package
for num_edges in  tqdm(range (num_runs)):
    num_cycs = 0
    for _ in range(epochs):
        graph = g.create_rand_graph_safe(num_nodes,num_edges)
        if g.has_cycle(graph):
            num_cycs += 1
            #print(graph.adj)
            #print (num_cycs)
    probs.append(num_cycs/epochs)

plt.plot(probs)
plt.show()
    


