class Binary_Tree():
    def __init__(self,size):
        self.custList = [None] * size
        self.lastUsedIdx = 0
        self.maxsize = size
    
    def insertion(self,value):
        if self.lastUsedIdx+1 == self.maxsize:
            return "Tree is full"
        self.custList[self.lastUsedIdx + 1] = value
        self.lastUsedIdx+=1
        return "Node inserted"
    
    def searching(self,value):
        for i in range(1,self.lastUsedIdx+1):
            if self.custList[i] == value:
                return self.custList[i],"value found"
        return "Not in Tree"
    
    def preOrder(self,idx):
        if idx > self.lastUsedIdx:
            return "Invalid idx"
        print(self.custList[idx])
        self.preOrder(idx*2)
        self.preOrder(idx*2+1)
    
    def inOrder(self,idx):
        if idx > self.lastUsedIdx:
            return "Invalid Idx"
        self.inOrder(idx*2)
        print(self.custList[idx])
        self.inOrder(idx*2+1)
    
    def postOrder(self,idx):
        if idx> self.lastUsedIdx:
            return "Invalid Idx"
        
        self.postOrder(idx*2)
        self.postOrder(idx*2+1)
        print(self.custList[idx])

    def levelOrder(self,idx):
        for i in range(idx,self.lastUsedIdx+1):
            print(self.custList[i])
    
    def delNode(self,value):
        for i in range(1,self.lastUsedIdx+1):
            if self.custList[i] == value:
                deepestNode = self.custList[self.lastUsedIdx]
                self.custList[i] = deepestNode
                self.custList[self.lastUsedIdx] = None
                self.lastUsedIdx -=1
                return "Node Deleted"
        return "Not found value"
    
    def delAll(self):
        self.custList = None
        self.lastUsedIdx = None
        self.maxsize = None

btl = Binary_Tree(8)
print(btl.insertion("drinks"))
print(btl.insertion("hot"))
print(btl.insertion("cold"))
print(btl.insertion("tea"))
print(btl.insertion("coffee"))
print(btl.insertion("cola"))
print(btl.insertion("fanta"))
# print(btl.searching("fanta"))
# print(btl.searching("fizz"))
# print(btl.preOrder(1))
# print()
# print(btl.inOrder(1))
# print()
# print(btl.postOrder(1))
# print()
# print(btl.levelOrder(1))
print(btl.delNode("fanta"))
print(btl.levelOrder(1))
print(btl.delNode("fizz"))
print(btl.delAll())
print(btl.levelOrder(1))