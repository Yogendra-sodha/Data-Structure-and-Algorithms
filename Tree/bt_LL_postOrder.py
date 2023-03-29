class TreeNode():
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

root = TreeNode("drinks")
cold = TreeNode("cold")
hot = TreeNode("hot")
root.leftchild = cold
root.rightchild = hot
cola = TreeNode("cola")
fanta = TreeNode("fanta")
cold.leftchild = cola
cold.rightchild = fanta
tea = TreeNode("tea")
coffee = TreeNode("coffee")
hot.leftchild = tea
hot.rightchild = coffee

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)
 
postOrderTraversal(root)
