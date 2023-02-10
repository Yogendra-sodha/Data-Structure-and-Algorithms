class Multistack:
    def __init__(self,stacksize):
        self.stackele = 3
        self.custlist = [0]*(stacksize*self.stackele)
        self.eachStacksize = [0]*self.stackele
        self.stacksize = stacksize

    def isFull(self,stacknum):
        if self.eachStacksize[stacknum] == self.stackele:
            return True
        else:
            return False
            
    def isEmpty(self,stacknum):
        if self.eachStacksize[stacknum] == 0:
            return True
        else:
            return False

    def helperTopmethod(self,stacknum):
        offset = self.stacksize * stacknum
        return offset + (self.eachStacksize[stacknum]-1)

    def push(self,value,stacknum):
        if self.isFull:
            return "The stack is full"
        else:
            self.eachStacksize[stacknum]+=1
            self.custlist[self.helperTopmethod(stacknum)] = value

    def pop(self,stacknum):
        if self.isEmpty:
            return "Stack is empty"
        else:
            value = self.custlist[self.helperTopmethod(stacknum)]
            self.custlist[self.helperTopmethod(stacknum)]=0
            self.eachStacksize -=1
            return value
    def peek(self,stacknum):
        if self.isEmpty:
            return "stack is empty"
        else:
            value = self.custlist[self.helperTopmethod(stacknum)]
            return value

csMultistack = Multistack(4)
print(csMultistack.helperTopmethod(3))
        
