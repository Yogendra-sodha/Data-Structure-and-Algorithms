class Queue():
    def __init__(self):
        self.list = []
    
    def __len__(self):
        return len(self.list)

    def push(self,item):
        self.list.append(item)
    
    def pop(self):
        return self.list.pop()
    
class StackviaQueue():
    def __init__(self):
        self.inStack = Queue()
        self.outStack = Queue()
    
    def enqueue(self,item):
        self.inStack.push(item)
    
    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result

customQueue = StackviaQueue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
customQueue.enqueue(4)
print(customQueue.dequeue())
