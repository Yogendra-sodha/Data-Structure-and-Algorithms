class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in self.list]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def add(self,x):
        self.list.append(x)
        return "Added value to stack"
    
    def pop(self):
        self.list.pop()
    
    def peek(self):
        return self.list[-1]

    def delete(self):
        self.list = None

csStack = Stack()
csStack.add(2)
csStack.add(3)
csStack.add(4)
csStack.add(55)
csStack.pop()
print(csStack)