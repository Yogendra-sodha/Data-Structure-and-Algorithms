class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
    
class ll():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

class Queue():
    def __init__(self):
        self.queue = ll()
    
    def __str__(self):
        nodes = [str(x.data) for x in self.queue]
        return "->".join(nodes)
    
    def isEmpty(self):
        if self.queue.head == None:
            return True
        else:
            return False

    def enqueue(self,item):
        newNode = Node(item)
        if self.queue.head == None:
            self.queue.head = newNode
            self.queue.tail = newNode
        else:
            self.queue.tail.next = newNode
            self.queue.tail = newNode
    
    def dequeue(self):
        if self.isEmpty():
            return True
        else:
            value = self.queue.head
            if self.queue.head == self.queue.tail :
                self.queue.head = None
                self.queue.tail = None
            else:
                self.queue.head = self.queue.head.next
            return value


class TreeNode():
    def __init__(self,name):
        self.name = name
        self.leftchild = None
        self.rightchild = None

rootValue = TreeNode("Drinks")
hot = TreeNode("hot")
cold = TreeNode("cold")
rootValue.leftchild = cold
rootValue.rightchild = hot
cola = TreeNode("cola")
fanta = TreeNode("fanta")
cold.leftchild = cola
cold.rightchild = fanta
tea = TreeNode("tea")
coffee = TreeNode("coffee")
hot.leftchild = tea
hot.rightchild = coffee

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    cq = Queue()
    cq.enqueue(rootNode)
    
    while not(cq.isEmpty()):
        value = cq.dequeue()
        print(value.data.name)

        if value.data.leftchild is not None:
            cq.enqueue(value.data.leftchild)

        if value.data.rightchild is not None:
            cq.enqueue(value.data.rightchild)

def searchNode(rootNode, nodeValue):
    if not rootNode:
        return
    
    else:
        cq = Queue()
        cq.enqueue(rootNode)
        while not(cq.isEmpty()):
            root = cq.dequeue()

            if root.data.name == nodeValue:
                return root.data.name,"found in binary tree"
            if root.data.leftchild:
                cq.enqueue(root.data.leftchild)
            if root.data.rightchild:
                cq.enqueue(root.data.rightchild)
    return "value not found in bt"

searchNode(rootValue,"cola")