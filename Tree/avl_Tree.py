import sys

sys.path.append('c:/Users/yuvis/Downloads/Stevens/DSA/Data-Structure-and-Algorithms/Stack')

# from ll_Queue import Queue
class Node:
    def __init__(self, data=None):
        self.data = data
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

class avl:
    def __init__ (self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1

def search(rootNode,nodevalue):
    if rootNode.data == nodevalue:
        return "value found"
    elif rootNode.data > nodevalue:
        if rootNode.leftchild.data == nodevalue:
            return "value found left subtree"
        else:
            search(rootNode.leftchild,nodevalue)
    else:
        if rootNode.rightchild.data == nodevalue:
            return " value found in right subtree"
        else:
            search(rootNode.rightchild,nodevalue)

def levelOrder(rootNode):
    if not rootNode:
        return
    
    else:
        cq = Queue()
        cq.enqueue(rootNode)

        while not(cq.isEmpty()):
            # import pdb
            # pdb.set_trace()
            root = cq.dequeue()
            print(root.data.data)

            if root.data.leftchild is not None :
                cq.enqueue(root.data.leftchild)
            if root.data.rightchild is not None:
                cq.enqueue(root.data.rightchild)

def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.leftchild)
    preOrder(rootNode.rightchild)



def right_rotate(disbalancedNode):
    newRoot = disbalancedNode.leftchild
    disbalancedNode.leftchild = disbalancedNode.leftchild.rightchild
    newRoot.rightchild = disbalancedNode
    disbalancedNode.height = 1 + max(get_height(disbalancedNode.leftchild),get_height(disbalancedNode.rightchild))
    newRoot.height = 1 + max(get_height(disbalancedNode.leftchild),get_height(disbalancedNode.rightchild))
    return newRoot

def left_rotate(disbalancedNode):
    newRoot = disbalancedNode.rightchild
    disbalancedNode.rightchild = disbalancedNode.rightchild.leftchild
    newRoot.leftchild = disbalancedNode
    disbalancedNode.height = 1 + max(get_height(disbalancedNode.leftchild), get_height(disbalancedNode.rightchild))
    newRoot.height = 1 + max(get_height(newRoot.leftchild),get_height(newRoot.rightchild))
    return newRoot

def get_height(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def get_balance(rootNode):
    if not rootNode:
        return 0
    return get_height(rootNode.leftchild) - get_height(rootNode.rightchild)

def insertNode(rootNode,nodeValue):
    if not rootNode:
        return avl(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftchild = insertNode(rootNode.leftchild,nodeValue)
    else:
        rootNode.rightchild = insertNode(rootNode.rightchild,nodeValue)
    
    rootNode.height = 1 + max(get_height(rootNode.leftchild),get_height(rootNode.rightchild))
    balance = get_balance(rootNode)

    if balance > 1 and nodeValue < rootNode.leftchild.data:
        return right_rotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftchild.data:
        rootNode.leftchild = left_rotate(rootNode.leftchild)
        return right_rotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightchild.data:
        return left_rotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightchild.data:
        rootNode.rightchild = right_rotate(rootNode.rightchild)
        return left_rotate(rootNode)
    return rootNode

def minValue(rootNode):
    if not rootNode or rootNode.leftchild is None:
        return rootNode
    return minValue(rootNode.leftchild)

def deleteNode(rootNode,nodeValue):
    if not rootNode:
        return rootNode
    
    elif nodeValue < rootNode.data:
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
        balance = get_balance(rootNode)
        if balance > 1 and get_balance(rootNode.leftchild) >= 0:
            return right_rotate(rootNode)
        if balance > 1 and get_balance(rootNode.leftchild) <= 0:
            rootNode.leftchild = left_rotate(rootNode.leftchild)
            return right_rotate(rootNode)
        if balance < -1 and get_balance(rootNode.rightchild) <= 0:
            return left_rotate(rootNode)
        if balance < -1 and get_balance(rootNode.rightchild) > 0:
            rootNode.rightchild = right_rotate(rootNode.rightchild)
            return left_rotate(rootNode)
    
    return rootNode





cs = avl(5)
cs = insertNode(cs,10)
cs = insertNode(cs,15)
cs = insertNode(cs,20)
cs = insertNode(cs,30)
cs = insertNode(cs,9)
cs = deleteNode(cs,20)
print(levelOrder(cs))