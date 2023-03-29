class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        string = str(self.value)
        if self.next:
            string+= ','+str(self.next)
        return string

class minStack:
    def __init__(self):
        self.top = None
        self.minNode = None

    def minValueNode(self):
        if not self.minNode :
            return False
        return self.minNode.value
    
    def push(self,item):
        if self.minNode and self.minNode.value< item:
            self.minNode = Node(value = self.minNode.value,next=self.minNode)
        else:
            self.minNode = Node(value = item,next = self.minNode)
        self.top = Node(value=item,next=self.top)

    def pop(self):
        if self.top.value == self.minNode.value:
            self.minNode = self.minNode.next
            self.top = self.top.next
        else:
            self.top = self.top.next
        

mincs = minStack()
mincs.push(2)
mincs.push(5)
mincs.push(3)
# mincs.push(1)
mincs.push(0)
# print(mincs.minValueNode())
mincs.pop()
print(mincs.minValueNode())
