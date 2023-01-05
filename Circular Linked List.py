class Node :
    def __init__(self,data=None):
        self.data = data
        self.next = None

class CLL:
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

    def createCLL(self,value):
        newNode = Node(value)
        # As this is only node we have in our circular linked list so we have to create reference to itself for next node.
        newNode.next = newNode
        self.head = newNode
        self.tail = newNode
        print("Intialiaze intitiated")

    def insertionCLL(self,nodeValue,location):
        if self.head == None:
            print("empty list")
            return "CSLL is empty"
        else :
            newNode = Node(nodeValue)
            if location == 0:
                print("location is first")
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            if location == 1:
                print("location is last")
# create connection between previous tail last reference was first node so here create conncetion of new tail's next reference to first node
                newNode.next = self.tail.next 
# Create conncetion old tails next reference as it is last reference. As old self.tail.next is last reference so last reference would be new tail refernce
                self.tail.next = newNode
# Now assign new tail after referencing tail refernce to first node, old tail last refernece to new tail and after assign self.tail is newNode 
                self.tail = newNode
            else :
                temp = self.head
                idx = 0
                while idx < location - 1:
                    print("Location is between")
                    temp = temp.next
                    idx+=1
                # Storing new location's next reference in next node as current Node next reference is temp.next
                nextNode = temp.next
                # Assigning current node's next reference NewNode to insert
                temp.next = newNode
                # Now assigning NewNode's next reference which is stored in nextNode variable
                newNode.next = nextNode
    
    def traverse(self):
        if self.head is None :
            print("Empty Link List")
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            if temp == self.tail.next:
                break
    def search(self,value):
        if self.head is None:
            print("Empty list")
        else :
            temp = self.head
            while temp is not None:
                if temp.data == value:
                    print("Found",value)
                    break
                else:
                    temp = temp.next
                    if temp == self.tail.next:
                        print("Value not in Linked List")
                        break
    def deletion(self,location):
        if self.head is None :
            print("List is empty")
        else :
            if location == 0 :
                if self.head == self.tail :
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else :
                    self.head = self.head.next
                    self.tail.next = self.head
            if location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    temp = self.head
                    while temp is not None:
                        if temp.next == self.tail:
                            break # This break statement will break whole while loop
                        temp = temp.next
                    temp.next = self.head
            else:
                temp = self.head
                idx = 0
                while idx < location - 1:
                    temp = temp.next
                    idx+=1
                nextNode = temp.next
                temp.next = nextNode.next
    def formatCLL(self):
        self.head = None
        self.tail.next = self.head or 1
        self.tail = None


c = CLL()
c.createCLL(2)
c.insertionCLL(1,0)
c.insertionCLL(3,1)
c.insertionCLL(4,2)
c.traverse()
# c.search(5)
# c.deletion(2)
print([node.data for node in c])
c.formatCLL()
print([node.data for node in c])
    




















