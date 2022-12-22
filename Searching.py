class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None # next is second variable to store the next variable
class SingleLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None :
                temp = temp.next
            temp.next = newNode
    def traverse(self):
        if self.head == None:
            print("List is empty")
        else :
            node = self.head 
            while node is not None :
                print(node.data)
                node = node.next 
    def delFirst(self):
        if self.head is None :
            print("List is empty")
        else :
            self.head = self.head.next

ss = SingleLL()
ss.insert(11)
ss.insert(21)
ss.traverse()
ss.delFirst()
ss.traverse()