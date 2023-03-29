class TreeNode():
    def __init__(self,data):
        self.data = data
        self.rightChild = None
        self.leftChild = None
    
bt = TreeNode("drink-root")
cold = TreeNode("cold")
bt.leftChild = cold
hot = TreeNode("hot")
bt.rightChild = hot
cola = TreeNode("cola")
fanta = TreeNode("Fanta")
cold.leftChild = cola
cold.rightChild = fanta
tea = TreeNode("tea")
coffee = TreeNode("coffee")
hot.leftChild = tea
hot.rightChild = coffee

def preOrderTraverse(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraverse(rootNode.leftChild)
    preOrderTraverse(rootNode.rightChild)

preOrderTraverse(bt)