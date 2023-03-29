class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
    
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode
    
    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.linkedList.head
    
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None

class binary_search_tree:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

def insertion(rootNode,value):
    if rootNode.data == None:
        rootNode.data = value
    elif value <= rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild = binary_search_tree(value)
        else:
            insertion(rootNode.leftchild,value)
    elif value >= rootNode.data:
        if rootNode.rightchild is None:
            rootNode.rightchild = binary_search_tree(value)
            
        else:
            insertion(rootNode.rightchild,value)
    return "Node inserted"

def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.leftchild)
    preOrder(rootNode.rightchild)    

def searchNode(rootNode,nodeValue):
    if not rootNode:
        return
    elif rootNode.data == nodeValue:
        return "Node value found"
    elif nodeValue < rootNode.data:
        if rootNode.leftchild == nodeValue:
            print("value Found")
        else:
            searchNode(rootNode.leftchild,nodeValue)
    elif nodeValue > rootNode.data:
        if rootNode.rightchild == nodeValue:
            print("value found in rightsubtree")
        else:
            searchNode(rootNode.rightchild,nodeValue)


def levelOrder(rootNode):
    if not rootNode:
        return

    else:
        cq = Queue()
        cq.enqueue(rootNode)
        while not(cq.isEmpty()):
            root = cq.dequeue()
            print(root.value.data)

            if root.value.leftchild is not None:
                cq.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                cq.enqueue(root.value.rightchild)


def minValue(bstn):
    currentNode = bstn
    while currentNode.leftchild is not None:
        currentNode = currentNode.leftchild
    return currentNode

def deleteNode(rootNode,nodeValue):
    if rootNode is None:
        return rootNode
    
    if nodeValue < rootNode.data :
        rootNode.leftchild = deleteNode(rootNode.leftchild,nodeValue)
    
    elif nodeValue > rootNode.data:
        rootNode.rightchild = deleteNode(rootNode.rightchild,nodeValue)
    
    else:
        if rootNode.leftchild is None:
            temp = rootNode.rightchild
            rootNode = None
            return temp
        
        if rootNode.rightchild is None:
            temp = rootNode.leftchild
            rootNode = None
            return temp
        
        temp = minValue(rootNode.rightchild)
        rootNode.data = temp.data
        rootNode.rightchild = deleteNode(rootNode.rightchild,temp.data)
        
    return rootNode

bst = binary_search_tree(None)
insertion(bst,50)
insertion(bst,99)
insertion(bst,30)
insertion(bst,40)
insertion(bst,90)
insertion(bst,20)
insertion(bst,80)
insertion(bst,85)
print(deleteNode(bst,50))
print()
levelOrder(bst)
print()
