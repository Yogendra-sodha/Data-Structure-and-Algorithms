class Hash:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def getHash(self,word):
        total = 0
        for i in word:
            total += ord(i)
        return total % self.max
    
    def add(self,key,val):
        h = self.getHash(key)
        self.arr[h] = val

        
    def get(self,key):
        h = self.getHash(key)
        return self.arr[h]