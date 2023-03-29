class AnimalShelter:
    def __init__(self):
        self.dog = []
        self.cat = []
        self.dogCat = []

    def enqueue(self,item,type):
        if type.lower() == "cat":
            self.cat.append(item)
        if type.lower() == "dog":
            self.dog.append(item)
        else:
            return "Not valid Animal"
        
    def dequeue(self,type):
        if type.lower() == "cat":
            return self.cat.pop(0)
        if type.lower() == "dog":
            return self.dog.pop(0)
        else:
            return "Not available this animal"
    
    def dequeueAny(self):
        self.dogCat = self.cat+self.dog
        return self.dogCat

    
asq = AnimalShelter()
asq.enqueue('cat1','cat')
asq.enqueue('dog1','dog')
asq.enqueue('cat2','cat')
print(asq.dequeue('dog'))
print(asq.dequeueAny())