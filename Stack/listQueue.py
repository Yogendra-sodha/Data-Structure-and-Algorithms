class Queue:

    def __init__(self,maxSize):
        self.list = []
        self.maxSize = maxSize
    
    def __str__(self):
        values = [str(x) for x in self.list]
        return str(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def enqueue(self,value):
        if len(self.list) == self.maxSize:
            return "Queue Full"
        else:
            self.list.append(value)
            return "Added to Queue"
    
    def dequeue(self):
        self.list.pop(0)

    def peek(self):
        return self.list[0]

    def delete(self):
        a = input("Are you sure you want to delete entire queue ? Y or N : ")
        if a.lower() == "y":
            self.list = None
            return "Deleted Queue"
        else:
            return "Aborted, Deletion !!"

qu = Queue(3)
print(qu.isEmpty())
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(1)
print(qu.enqueue(8))
print(qu)