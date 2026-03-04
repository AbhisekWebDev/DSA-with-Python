n = 6 # no of nodes
e = 7 # no of edges

edges = [(0,1), (0,3), (0,4), (1,2), (1,5), (2,4), (3,4)] # edges

print(n,e,edges)

print("Adjacency Matrix:")

adjMatrix = []

for i in range(n) :
    adjMatrix.append([-1] * n) # create empty matrix for each node

for i in range(n) :
    x = edges[i][0]
    y = edges[i][1]

    adjMatrix[x][y] = 1 # set adjacency matrix value to 1
    adjMatrix[y][x] = 1 # set adjacency matrix value to 1

for i in adjMatrix :
    print(i)

