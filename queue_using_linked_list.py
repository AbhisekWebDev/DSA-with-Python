class ListNode :
    
    def __init__(self, data) :
        self.data = data
        self.next = None

class Queue :
    
    def __init__ (self) :
        self.front = None
        self.rear = None

    def enqueue (self, x) :
        newNode = ListNode(x)

        if self.rear is None :
            self.front = self.rear = newNode
            return
        
        else :
            self.rear.next = newNode
            self.rear = newNode

    def dequeue (self) :
        
        if self.is_empty() :
            return None
        
        temp = self.front
        self.front = temp.next

        if self.front is None :
            self.rear = None

        return temp.data
    
    def getFront (self) :

        if self.is_empty() :
            return None
        
        return self.front.data
    
    def getRear (self) :

        if self.is_empty() :
            return None
        
        return self.rear.data
    
    def is_empty (self) :
        return self.front is None
    
    def printQueue (self) :

        temp = self.front

        while temp :

            print(temp.data, end = " ")

            temp = temp.next
        
        print()

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.printQueue()      # 1 2 3 4 5

q.dequeue()
q.printQueue()      # 2 3 4 5

print(q.getFront()) # 2
print(q.getRear())  # 5
