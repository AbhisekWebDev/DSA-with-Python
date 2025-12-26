from collections import deque
q = deque()
q.append(10)
q.popleft()
q.append(20)
q.popleft()
q.append(30)
print(q)  # Output: deque([30])


# Used in:

# Level Order Tree Traversal

# BFS

# Processing Tasks

# Print the queue after each operation to see the state

