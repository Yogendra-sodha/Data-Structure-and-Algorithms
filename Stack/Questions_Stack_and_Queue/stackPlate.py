class stackPlate:

    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = []
    
    def __str__(self):
        return self.stacks

    def push(self,item):
        if len(self.stacks)>0 and len(self.stacks[-1])< self.capacity:
            self.stacks[-1].append(item)
        
        else:
            self.stacks.append([item])
        
    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            self.stacks[-1].pop()
    
    def pop_at(self,stackNumber):
        if len(self.stacks[stackNumber]) == 0 :
            return "Stack is empty"
        else:
            self.stacks[stackNumber].pop()

csPlate = stackPlate(2)
csPlate.push(2)
csPlate.push(3)
csPlate.push(1)
csPlate.push(6)
csPlate.push(8)
csPlate.push(7)
print(csPlate.pop())
print(csPlate.pop_at(1))
print(csPlate.stacks)