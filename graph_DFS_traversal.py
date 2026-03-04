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

# stack bnate h
class Stack :
    def __init__ (self) :
        self.st = []

    def push(self, x) :
        self.st.append(x)
    
    def pop(self) :
        if len(self.st) == 0 :
            return None
        return self.st.pop() # pop from end of list

stack = Stack()

visited = [False] * n # visited array

ans = [] # to store DFS traversal

stack.push(0) # start DFS from node 0
visited[0] = True
ans.append(0)

while len(stack.st) > 0 :
    top = stack.pop()
    for neighbour in adjList[top] :
        if not visited[neighbour] :
            stack.push(neighbour)
            visited[neighbour] = True
            ans.append(neighbour)

print(ans) 