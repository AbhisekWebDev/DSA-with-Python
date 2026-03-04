n = 6 # no of nodes
e = 7 # no of edges

edges = [(0,1), (0,3), (0,4), (1,2), (1,5), (2,4), (3,4)] # edges

print(n,e,edges)

print("Adjacency List:")

adjList = []

for i in range(n) :
    adjList.append([]) # create empty list for each node

for edge in edges :
    x = edge[0]
    y = edge[1]

    adjList[x].append(y) # add y to x's list
    adjList[y].append(x) # add x to y's list

for i in range(n) :
    print(i, "->", adjList[i])