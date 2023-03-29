class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class llQ:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

class Queue:
    def __init__(self):
        self.llq = llQ()

    def __str__(self):
        values = [str(x) for x in self.llq]
        return "->".join(values)

    def isEmpty(self):
        if self.llq.head == None:
            return True
        else:
            return False
    
    def enqueue(self,value):
        newNode = Node(value)
        if self.llq.head == None:
            self.llq.head = newNode
            self.llq.tail = newNode

        else:
            self.llq.tail.next = newNode
            self.llq.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            return "It is empty"
        
        if self.llq.head == self.llq.tail:
            self.llq.head = None
            self.llq.tail = None
        else:
            self.llq.head = self.llq.head.next

    def peek(self):
        if self.isEmpty():
            return "llq is empty"
        else:
            return self.llq.head.data
    
    def delete(self):
        self.llq.head = None
        self.llq.tail = None
        return "Queue cleared"

# csllq = Queue()
# (csllq.enqueue(2))
# (csllq.enqueue(3))
# (csllq.enqueue(1))
# print(csllq.delete())