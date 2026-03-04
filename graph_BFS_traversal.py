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

print("BFS Traversal:") # BFS is implemented using queue

# queue bnate h
class Queue :
    def __init__ (self) :
        self.q = []
        self.front = -1

    def push(self, x) :
        self.q.append(x)
        if self.front == -1 :
            self.front = 0
    
    def pop(self) :
        if self.front == -1 :
            return None
        x = self.q[self.front]
        self.front += 1
        if self.front >= len(self.q) :
            self.front = -1
            self.q = []
        return x
    
q = Queue()

visited = [False] * n # visited array

ans = [] # to store BFS traversal

q.push(0) # start BFS from node 0
visited[0] = True
ans.append(0)

while q.front != -1 :
    front = q.pop()
    for neighbour in adjList[front] :
        if not visited[neighbour] :
            q.push(neighbour)
            visited[neighbour] = True
            ans.append(neighbour)

print(ans) 

# note - traversal ka order matter nhi krta h