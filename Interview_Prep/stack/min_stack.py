class MinStack:

    def __init__(self):

        self.stack = []      # main stack
        self.min_stack = []  # keeps track of minimums
        

    def push(self, val: int) -> None:

        self.stack.append(val)

        # if min_stack empty, val is min
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        

    def pop(self) -> None:

        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:

        return self.stack[-1]
        

    def getMin(self) -> int:
        
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()