import random
from datetime import datetime

test_data = 'test_data.txt'
graph = {}  # the whole graph will be stored in a dictionary
# read data from test data
with open(test_data, 'rb') as fp:
    for line in fp:
        nums = [int(num) for num in line.split()]
        node = nums[0]
        edges = nums[1:]
        graph[node] = edges


def karger(graph):
    while len(graph) > 2:
        # at last, there will be only 2 nodes left in the graph
        random.seed(datetime.now())
        start = random.choice(list(graph))
        # randomly selecting a finish node
        finish = random.choice(graph[start])

        for edge in graph[finish]:
            # self-loop prevention
            if edge != start:
                # merge all edges that connected to finish node to start
                graph[start].append(edge)

        # delete 'finish' from other nodes that were connected with 'finish'
        for edge in graph[finish]:
            graph[edge].remove(finish)
            # adding these nodes to 'start', but not 'start' itself
            if edge != start:
                graph[edge].append(start)
        # remove 'finish' at last
        del graph[finish]
    # at last, there will be only two nodes in the graph
    # the number of edges of either node is a possible min_cut
    for key in graph:
        return(len(graph[key]))

min_cut = 100000
# iterate 100000 times
for i in range(100000):
    cut = karger(graph)
    if min_cut > cut:
        min_cut = cut
print(min_cut)
