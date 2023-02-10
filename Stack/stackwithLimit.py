class Stack:

    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self,data):
        if len(self.list) == self.maxSize:
            return "Stack full"
        else:
            self.list.append(data)

    def pop(self):
        self.list.pop()
    
    def delete(self):
        self.list = None

cst = Stack(3)
cst.push(1)
cst.push(2)
cst.push(3)
print(cst.push(4))
print(cst)
