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
        root = cq.dequeue()
        print(root.data.name)

        if root.data.leftchild is not None:
            cq.enqueue(root.data.leftchild)

        if root.data.rightchild is not None:
            cq.enqueue(root.data.rightchild)

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

# print(searchNode(rootValue,"cola"))

def insertion(rootNode,newNode):
    if not rootNode:
        return
    cq = Queue()
    cq.enqueue(rootNode)
    while not(cq.isEmpty()):
        root = cq.dequeue()
        if root.data.leftchild == None:
            root.data.leftchild = newNode
            return newNode.name,"inserted in left subtree"
        else:
            cq.enqueue(root.data.leftchild)

        if root.data.rightchild == None:
            root.data.rightchild = newNode
            return newNode.name,"inserted in right subtree"
        else:
            cq.enqueue(root.data.rightchild)


def getDeepestNode(rootNode):
    if rootNode is None:
        return
    else:
        cq = Queue()
        cq.enqueue(rootNode)
        while not(cq.isEmpty()):
            root = cq.dequeue()

            if root.data.leftchild is not None:
                cq.enqueue(root.data.leftchild)
            if root.data.rightchild is not None:
                cq.enqueue(root.data.rightchild)
        dnode = root.data
        return dnode

# print(getDeepestNode(rootValue))
newNode = TreeNode("cherry-coke")
insertion(rootValue,newNode)
# print(getDeepestNode(rootValue))

def delDeepestNode(rootNode,dNode):
    if rootNode is None:
        return
    else:
        cq = Queue()
        cq.enqueue(rootNode)
        while not(cq.isEmpty()):
            root = cq.dequeue()
            if root.data is dNode:
                root.data = None
                return

            if root.data.leftchild:
                if root.data.leftchild == dNode:
                    root.data.leftchild = None
                    return
                else:
                    cq.enqueue(root.data.leftchild)

            if root.data.rightchild is not None:
                if root.data.rightchild == dNode:
                    root.data.rightchild = None
                    return
                else:
                    cq.enqueue(root.data.rightchild)
        return "deleted deepest node"

# dNode = getDeepestNode(rootValue)
# print(delDeepestNode(rootValue,dNode))
# levelOrderTraversal(rootValue)

def deleteNode(rootValue,node):
    if rootValue is None:
        return
    else:
        cq = Queue()
        cq.enqueue(rootValue)

        while not(cq.isEmpty()):
            root = cq.dequeue()
            if root.data.name == node:
                dNode = getDeepestNode(rootValue)
                root.data.name = dNode.name
                delDeepestNode(rootValue,dNode)
                return "node deleted"
            if root.data.leftchild is not None:
                cq.enqueue(root.data.leftchild)
            if root.data.rightchild is not None:
                cq.enqueue(root.data.rightchild)

def delentireTree(rootNode):
    rootNode.name = None
    rootNode.leftchild = None
    rootNode.rightchild = None

# levelOrderTraversal(rootValue)
# print(deleteNode(rootValue,"hot"))
# print(levelOrderTraversal(rootValue))
print(delentireTree(rootValue))
print(levelOrderTraversal(rootValue))