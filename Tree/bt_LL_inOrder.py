class TreeNode():
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

root = TreeNode("drink")
cold = TreeNode("cold")
root.leftchild = cold
hot = TreeNode("hot")
root.rightchild = hot
cola = TreeNode("cola")
fanta = TreeNode("fanta")
cold.leftchild = cola
cold.rightchild = fanta
tea = TreeNode("tea")
coffee = TreeNode("coffee")
hot.leftchild = tea
hot.rightchild = coffee

def inOrderTraverse(rootNode):
    if not rootNode:
        return
    inOrderTraverse(rootNode.leftchild)
    print(rootNode.data)
    inOrderTraverse(rootNode.rightchild)

inOrderTraverse(root)