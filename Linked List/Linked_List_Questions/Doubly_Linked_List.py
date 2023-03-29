# Creation of Node
class Node:
    def __init__(self,data=None):
        self.data = data
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    # Creation of Double Linked List by creating First node with reference to its head and tail
    def creatDLL (self,value):
        newNode = Node(value)
        newNode.next = None
        newNode.prev = None
        # newNode.data = value  # Storing value in new node's data variable in new instance class created newNode
        self.head = newNode
        self.tail = newNode

    def insert(self,value,location):
        if self.head == None :
            print("DLL is empty")
        
        else:
            newNode = Node(value)
            if location == 0:
                # Creating new node prev location which would none as it is on first location
                newNode.prev = None
                # Creating new node with next reference as we adding node to first location
                newNode.next = self.head
                # Updating connection of old head prev location referencing to new node head location
                self.head.prev = newNode
                # Assiging new head as new node
                self.head = newNode

            elif location == 1:
                # new node next reference would be none as it is last node
                newNode.next = None
                # New node tail's previous would be old tail reference
                newNode.prev = self.tail
                # updating connextion of old tail next reference to new tail, so old tail.next would be new node
                self.tail.next = newNode
                # updating new tail as new node
                self.tail = newNode
            
            else :
                temp = self.head
                idx = 0
                while idx < location-1:
                    temp = temp.next
                    idx += 1
                newNode.next = temp.next
                newNode.prev = temp
                newNode.next.prev = newNode
                temp.next = newNode
    
    def traversal(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    def reverseTraversal(self):
        node = self.tail
        while node:
            print(node.data)
            node = node.prev

    def search(self,value):
        if self.head == None:
            print("List is empty")
        else :
            temp = self.head
            while temp:
                if temp.data == value:
                    return "Value found",temp.data
                temp = temp.next
            return "value not in DLL !"
    
    def deleteNode(self,location):
        if self.head == None :
            return "The DLL is empty"
        
        else:
            if location == 0 :
                if self.head == self.tail:
                    self.head = None
                    self.head.next = None
                    self.tail = None
                else :
                    self.head = self.head.next
                    self.head.prev = None

            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else :
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    temp = self.head
                    idx = 0
                    while idx<location-1:
                        temp = temp.next
                        idx += 1
                    nextNode = temp.next
                    temp.next = nextNode.next # or temp.next.next
                    temp.next.prev = temp
                    # nextNode.prev = None # Not needed
    
    def formatDLL(self):
        if self.head is None:
            return "Empty!"
        else:
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next
            self.head = None
            self.head = None

d = DLL()
d.creatDLL(2)
# print([node.data for node in d])
d.insert(0,0)
# print([node.data for node in d])
d.insert(3,1)
# print([node.data for node in d])
d.insert(4,2)
print([node.data for node in d])
d.deleteNode(2)
print([node.data for node in d])
d.formatDLL()
print([node.data for node in d])
# d.traversal()
# d.reverseTraversal()
# print(d.search(33))