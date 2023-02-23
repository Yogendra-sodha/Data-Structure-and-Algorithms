import os

cwd = os.getcwd()
print(cwd)
# sys.path.append("C:\\Users\\yuvis\\Downloads\\Stevens\\DSA")
# print(sys.path)
# from Stack import ll_Queue

# l = ll_Queue.Queue()
# print(l.dequeue())


# class avl:
#     def __init__ (self,data):
#         self.data = data
#         self.leftchild = None
#         self.rightchild = None
#         self.height = 1

# def search(rootNode,nodevalue):
#     if rootNode.data == nodevalue:
#         return "value found"
#     elif rootNode.data > nodevalue:
#         if rootNode.leftchild.data == nodevalue:
#             return "value found left subtree"
#         else: 
#             search(rootNode.leftchild,nodevalue)
#     elif rootNode.data < nodevalue:
#         if rootNode.rightchild.data == nodevalue:
#             return " value found in right subtree"
#         else:
#             search(rootNode.rightchild,nodevalue)

# def levelOrder(rootNode):
#     if not rootNode:
#         return
    
#     else:
#         cq = ll_Queue.llQ()
#         cq.enqueue(rootNode)

#         while not(cq.isEmpty()):
#             root = cq.dequeue(rootNode)
#             print(root.data.data)

#             if rootNode.data.leftchild is not None :
#                 cq.enqueue(rootNode.data.leftchild)
#             if rootNode.data.rightchild is not None:
#                 cq.enqueue(rootNode.data.rightchild)

# def preOrder(rootNode):
#     if not rootNode:
#         return
    
#     print(rootNode.data.data)
#     preOrder(rootNode.data.leftchild)
#     preOrder(rootNode.data.rightchild)

# def get_height(rootNode):
#     if not rootNode:
#         return 0
#     return rootNode.height

# def left_rotate(disbalancedNode):
#     newRoot = disbalancedNode.rightchild
#     disbalancedNode.rightchild = disbalancedNode.rightchild.leftchild
#     newRoot.rightchild = disbalancedNode
#     disbalancedNode.height = 1 + max(get_height(disbalancedNode.leftchild), get_height(disbalancedNode.rightchild))
#     newRoot.height = 1 + max(get_height(newRoot.leftchild),get_height(newRoot.rightchild))
#     return newRoot

# def right_rotate(disbalancedNode):
#     newRoot = disbalancedNode.leftchild
#     disbalancedNode.leftchild = disbalancedNode.leftchild.rightchild
#     newRoot.leftchild = disbalancedNode
#     disbalancedNode.height = 1 + max(get_height(disbalancedNode.leftchild),get_height(disbalancedNode.rightchild))
#     newRoot.height = 1 + max(get_height(disbalancedNode.leftchild),get_height(disbalancedNode.rightchild))
#     return newRoot

# def get_balance(rootNode):
#     if not rootNode:
#         return 0
#     return get_height(rootNode.leftchild) - get_height(rootNode.rightchild)

# def insertNode(rootNode,nodeValue):
#     if not rootNode:
#         avl(nodeValue)
#         return "node value inserted in root"
#     elif nodeValue > rootNode.data:
#         insertNode(rootNode.leftchild,nodeValue)
#     else:
#         insertNode(rootNode.rightchild,nodeValue)
    
#     rootNode.height = 1 + max(get_height(rootNode.leftchild),get_height(rootNode.rightchild))
#     balance = get_balance(rootNode)

#     if balance > 1 and nodeValue < rootNode.leftchild.data:
#         return right_rotate(rootNode)
#     if balance > 1 and nodeValue > rootNode.leftchild.data:
#         rootNode.leftchild = left_rotate(rootNode.leftchild)
#         return right_rotate(rootNode)
#     if balance < -1 and nodeValue > rootNode.rightchild.data:
#         return left_rotate(rootNode)
#     if balance < -1 and nodeValue < rootNode.rightchild.data:
#         rootNode.rightchild = right_rotate(rootNode.rightchild)
#         return left_rotate(rootNode)
#     return rootNode


# cs = avl(None)

# print(insertNode(cs,5))