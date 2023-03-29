# binary heap is basically a binary tree with all levels filled except last level with all values to left side if possible in last level

class binaryHeap:
    def __init__(self,size):
        self.heapList = (size+1) * [None]
        self.heapsize = 0
        self.maxsize = size + 1

def peekHeap(rootNode):
    if not rootNode:
        return
    return rootNode.heapList[1]

def levelOrder(rootNode):
    if not rootNode:
        return
    for i in range(1,rootNode.heapsize+1):
        print(rootNode.heapList[i])

def heapifyTree(rootNode,index,type):
    parentIdx = int(index/2)

    if index <= 1:
        return
    
    if type == "min":
        if rootNode.heapList[parentIdx] > rootNode.heapList[index]:
            temp = rootNode.heapList[index]
            rootNode.heapList[index] = rootNode.heapList[parentIdx]
            rootNode.heapList[parentIdx] = temp
        heapifyTree(rootNode,parentIdx,type)

    elif type == "max":
        if rootNode.heapList[parentIdx] < rootNode.heapList[index]:
            rootNode.heapList[index],rootNode.heapList[parentIdx] = rootNode.heapList[parentIdx],rootNode.heapList[index]
        heapifyTree(rootNode,parentIdx,type)

def insertNode(rootNode,nodeValue,type):
    if rootNode.maxsize == rootNode.heapsize+1:
        return "Binary heap storage full"
    
    rootNode.heapList[rootNode.heapsize+1] = nodeValue
    rootNode.heapsize+=1
    heapifyTree(rootNode,rootNode.heapsize,type)
    return "Node inserted"

bheap = binaryHeap(5)
print(insertNode(bheap,10,"min"))
print(insertNode(bheap,5,"min"))
levelOrder(bheap)