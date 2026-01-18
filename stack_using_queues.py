from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # rotate
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        if self.empty():
            return None
        return self.q.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

    def display(self):
        print("Stack (top -> bottom):", list(self.q))


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


s = MyStack()

s.push(1)
s.push(2)
s.push(3)

s.display()  # [3, 2, 1]

s.pop()  # 3
s.display()  # [2, 1]

print(s.top())  # 2

print(s.empty())  # False


# When using deque as a queue, you are expected to use:

# append()    # enqueue (rear)
# popleft()  # dequeue (front)


# why not appendleft?

# Excellent question

# Short answer: you can use appendleft(), but then you’re no longer solving the “stack using queue” problem in its intended sense.

# dq.appendleft(x) - It inserts an element at the front in O(1) time.

# That means: Front insertion + front removal



# Why Interviewers Say “Don’t Use appendleft()” ?

# 1 It breaks the constraint

# In Stack using Queue, the implied constraint is:

# Use queue operations only

# Queue operations are:

# enqueue → push at rear

# dequeue → pop from front

# Using appendleft() gives you stack power for free.

# So this:

# dq.appendleft(x)


# is equivalent to saying:

# “I already have a stack.”



# 2 It defeats the purpose of the problem

# The whole point of the question is to test:

# FIFO → LIFO conversion

# Data structure manipulation

# Logical thinking

# If you do:

# push → appendleft
# pop → popleft


# Then:

# push = O(1)

# pop = O(1)

# That’s cheating (from an interview perspective).




# When IS appendleft() OK?
# In real-world / production code

# If the goal is efficiency, use it.

# Example:

# from collections import deque

# stack = deque()
# stack.appendleft(10)
# stack.appendleft(20)
# stack.popleft()  # 20


# Perfectly fine

# In DSA / interviews / exams

# Avoid it unless explicitly allowed.