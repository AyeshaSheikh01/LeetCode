class MyQueue:

    def __init__(self):
        self.queue=[] 
    def push(self, x: int): 
        self.queue.append(x)
    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0] 
    def empty(self) -> bool: 
        isEmpty=not bool(self.queue) 
        return isEmpty 

myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
myQueue.peek() 
myQueue.pop() 
myQueue.empty() 