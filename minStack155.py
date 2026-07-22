# Min stack - leetcode 155 
class MinStack:

    def __init__(self):
        self.stack=[] # initializing the stack first

    def push(self, val: int): 
        self.stack.append(val) # push
    def pop(self): 
        self.stack.pop() # pop
    def top(self): 
        return self.stack[-1] # top

    def getMin(self): 
        return min(self.stack) # minimum element in the stack 
    
minStack = MinStack() 
minStack.push(-2) 
minStack.push(0) 
minStack.push(-3) 
print(minStack.getMin())
minStack.pop()  
print(minStack.top())
print(minStack.getMin()) 
