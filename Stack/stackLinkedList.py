class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def __str__(self):
        values = [str(x.data) for x in self.ll]
        return '\n'.join(values)

    def isEmpty(self):
        if self.ll.head == None:
            return True
        else:
            return False
    
    def push(self,value):
        newNode = Node(value)
        newNode.next = self.ll.head
        self.ll.head = newNode

    def peek(self):
        return self.ll.head.data

    def pop(self):
        popNode = self.ll.head
        self.ll.head = self.ll.head.next
        return "the removed item is",popNode.data

    def delete(self):
        self.ll.head = None

cs = Stack()
# print(cs.isEmpty())
cs.push(2)
cs.push(4)
cs.push(7)
cs.pop()
print(cs)

