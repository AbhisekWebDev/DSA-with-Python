class ListNode :
    def __init__(self, data) :
        self.data = data
        self.next = None


class Stack :

    def __init__(self) :

        # head se hi push aur pop krenge isme
        # aur yaha pr top ka matlab head hi hoga

        self.top = None

        self.length = 0

    def push(self, x) :

        if self.top is None :

            self.length += 1
                
            # naya node bnayenge agr self.top empty rha to
            self.top = ListNode(x)

            return
            
        else :
                
            # ab current node k piche naya node add krenge
            newNode = ListNode(x)

            newNode.next = self.top
            self.top = newNode
        
    def pop(self) :

        self.length -= 1

        if self.top is None :
            return -1
            
        else:
                
            # pop krne wale node ko store kr lenge
                # aur self.top ko next pr move kr denge [aage wale node pr badha denge]
            poppedNode = self.top
            self.top = self.top.next

            return poppedNode.data
            

        
    def peek(self) :

        if self.top is None :
            return -1
            
        else:
            return self.top.data
            
    def size(self) :

        return self.length
    
    def printStack(self) :
        curr = self.top

        while curr is not None :
            print(curr.data, end = " ")
            curr = curr.next

        print()

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.top.data)

stack.printStack()

print(stack.pop())

print(stack.peek())

print(stack.size())