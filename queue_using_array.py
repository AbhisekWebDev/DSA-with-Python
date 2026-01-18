# FIFO

# front se push aur rear se pop

from collections import deque

# Using deque - deque is a specialized data structure in Python designed for fast appends and pops from both ends. Unlike regular lists, deque allows us to insert an element at the front efficiently, making it an ideal option for this operation.

q = deque([])

# enqueue
q.appendleft(1)
q.appendleft(2)
q.appendleft(3)
q.appendleft(4)
q.appendleft(5)

print(q)

# dequeue
q.pop()
print(q)

# front
print(q[-1])
# matlab last index

# rear
print(q[0])
# matlab first index