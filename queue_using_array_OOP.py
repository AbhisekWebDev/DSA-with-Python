class Queue :
    def __init__(self) :
        self.q = []
        self.front = -1

    def enqueue(self, x) :
        if self.front == -1 :
            self.front = 0
        
        self.q.insert(0, x)
    
    def dequeue (self) :
        if self.is_empty() :
            return None
        
        return self.q.pop()
    
    def get_front(self) :
        if self.is_empty() :
            return None
        
        return self.q[-1]  
    
    def get_rear (self) :
        if self.is_empty() :
            return None
        
        return self.q[0]
    
    def is_empty (self) :

        return len(self.q) == 0
    
    def __str__(self):
        
        return str(self.q)
    
    
q = Queue()

# enqueue
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q)

# dequeue
q.dequeue()

print(q)

# front
print(q.get_front())

# rear
print(q.get_rear())




