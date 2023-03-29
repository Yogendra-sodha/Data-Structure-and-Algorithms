class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None
class DCLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    def createDCLL(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode

    def insertDCLL(self,value,location):
        if self.head is None:
            return "List Empty!"
        else:
            newNode = Node(value)
            if location == 0 :
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1 :
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode # Old tail next reference
                self.tail = newNode # Assign it last as before self.tail is still old node
            else:
                temp = self.head
                idx = 0
                while idx<location-1 :
                    temp = temp.next
                    idx+=1
                newNode.next = temp.next
                newNode.prev = temp
                newNode.next.prev = newNode
                temp.next = newNode
                

d = DCLL()
d.createDCLL(5)
# print([node.data for node in d])
d.insertDCLL(0,0)
# print([node.data for node in d])
d.insertDCLL(1,1)
# print([node.data for node in d])
d.insertDCLL(2,2)
print([node.data for node in d])