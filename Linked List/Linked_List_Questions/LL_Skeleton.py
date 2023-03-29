from random import randint
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

class LinkedListBody:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def __str__(self):
        values = [str(x.data) for x in self]
        return "->".join(values)
    
    def __len__(self):
        temp = self.head
        result = 0
        while temp:
            temp = temp.next
            result += 1
        return result

    def add(self,value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode

        else :
            # Adding node at to the tail of LL
            self.tail.next = Node(value) # as tail next refernece would be null
            self.tail = self.tail.next # now tail's next refernce is new tail so assigning new tail
        return self.tail

    def generate(self,n,min_range,max_range):
        # Creating new node
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_range,max_range))
        return self