class LinkedList:
    def __init__(self,data=None):
        self.data = data
        self.nextdata = None

class operation:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,value):
        node = LinkedList(value)
        if self.head == None :
            self.head = node  # this will store object with data and next value the node class has
        else:
            temp = self.head
            while temp.nextdata is not None:
                # print(temp)
                temp = temp.nextdata
                # print(temp)
                # print(temp.nextdata)
            temp.nextdata = node
    def traverse (self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.nextdata
    def deletefirst(self):
        if self.head == None:
            print("Empty linked list")
        else :
            self.head = self.head.nextdata


c = operation()
c.insert(1)
c.insert(2)
c.insert(3)
c.insert(4)
c.traverse()
c.deletefirst()
c.traverse()