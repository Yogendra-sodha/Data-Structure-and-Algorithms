class Stack:
    def __init__(self,maxsize):
        self.list = []
        self.maxsize = maxsize
        
    def __str__(self):
        values = self.list[::-1]
        values = [str(x) for x in values]
        return "\n".join(values)

    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False

    def push(self,value):
        if self.isFull():
            return "Stack is Full"
        else :
            return self.list.append(value)
    
    def peek(self):
        return self.list[::-1]

    def remove(self):
        self.list = None

    def delete(self):
        if self.isEmpty():
            return "The stack is Empty"
        else:
            return self.list.pop()

    def isEmpty(self):
        if self.list == []:
            return True



customstack = Stack(2)
print(customstack.delete())

customstack.push(1)
customstack.push(2)
print(customstack.push(3))
# customstack.push(4)
print(customstack)