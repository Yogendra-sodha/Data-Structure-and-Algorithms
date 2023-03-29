class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Ll():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

class Stack_min():
    def __init__(self):
        self.stack = Ll()

    def __str__(self):
        values = [str(x.data) for x in self.stack]
        return "->".join(values)

    def isEmpty(self):
        if self.stack.head == None:
            return True
        else:
            return False
    

    def push(self,value):
        newNode = Node(value)
        newNode.next = self.stack.head
        self.stack.head = newNode
    
    def pop(self):
        popNode = self.stack.head
        self.stack.head = self.stack.head.next
        return "the removed item is",popNode.data

    def min(self):
        node = self.stack.head
        min_value = self.stack.head.data
        while node:
            if node.data<min_value:
                min_value = node.data
            node = node.next
        return min_value
        
cs = Stack_min()
cs.push(5)
cs.push(1)
cs.push(3)
cs.push(2)
print(cs.min())
print(cs)