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

print("DFS Traversal:") # DFS is implemented using stack

visited = [False] * n # visited array

ans = [] # to store DFS traversal

def dfsRecursive(currNode, parent, adjList, visited) :
    visited[currNode] = True
    ans.append(currNode)

    for neighbour in adjList[currNode] :

        if neighbour == parent : # if neighbour is parent, skip it
            continue

        if visited[neighbour] : # if neighbour is already visited, then we have found a cycle
            ans.append("Cycle Detected")
            return True
        
        if dfsRecursive(neighbour, parent, adjList, visited) :
            return True
        
    return False

dfsRecursive(0, -1, adjList, visited) # 0 se shuru kr rhe nodes ka traversal

print(ans)