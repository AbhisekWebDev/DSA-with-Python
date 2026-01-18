from collections import deque

class Queue:
    def __init__(self):
        
        self.q = deque()   # Use deque instead of list

    def enqueue(self, x):
        
        # Insert at left (front)
        self.q.appendleft(x)

    def dequeue(self):
        
        if self.is_empty():
            return None
        
        # Pop from right (rear)
        return self.q.pop()

    def get_front(self):
        
        if self.is_empty():
            return None
        
        # Front is at the right (last index)
        return self.q[-1]

    def get_rear(self):
        
        if self.is_empty():
            return None
        
        # Rear is at the left
        return self.q[0]

    def is_empty(self):
        
        return len(self.q) == 0

    def __str__(self):
        
        return str(list(self.q))   # convert to list for nice printing

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q)        # [4, 3, 2, 1]

q.dequeue()
print(q)        # [4, 3, 2]

print(q.get_front())  # 2

print(q.get_rear())   # 4
