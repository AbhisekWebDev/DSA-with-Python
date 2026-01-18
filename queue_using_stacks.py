class MyQueue:

    def __init__(self):

        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        
        # jabtak stack1 empty nhi hota
        while len(self.stack1) > 0 :
            
            # tabtak stack1 ka jo pop h wo stack2 me push krte rhenge
            self.stack2.append(self.stack1.pop())
        
        # ab stack1 me append krenge jo bhi extra element ayga
        self.stack1.append(x)

        # aur ab fir stack2 se pop kr k stack1 me push krenge

        # jabtak stack2 empty nhi hota
        while len(self.stack2) > 0 :
            
            # tabtak stack2 ka jo pop h wo stack1 me push krte rhenge
            self.stack1.append(self.stack2.pop())


    def pop(self) -> int:

        if self.empty():
            return None

        # last index
        x = self.stack1[-1] 
        self.stack1.pop()
        return x
        

    def peek(self) -> int:

        if self.empty():
            return None

        return self.stack1[-1] 
        

    def empty(self) -> bool:
        return len(self.stack1) == 0
    
    def display(self) :
        if self.empty():
            print("Queue is empty")
            return

        # front -> rear
        print("Queue:", self.stack1[::-1])
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

q = MyQueue()

q.push(10)
q.push(20)
q.push(30)

q.display()

print(q.peek())   # 10
print(q.pop())    # 10
print(q.pop())    # 20
print(q.empty())  # False

q.display()
