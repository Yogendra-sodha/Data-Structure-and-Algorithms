# # Trie is a data structure used to string in hierachial way like a tree. any node in tree can store multiple non repitve character.Every
# # node keeps track of end of string.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        current = self.root

        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endString = True
        return "Word inserted"

    def search(self,word):
        current = self.root

        for i in word:
            node = current.children.get(i)
            if node == None:
                return False
            current = node

        if current.endString == True:
            return "String Exists"
        return "String does not exists"

def delete(root,word,idx):
    ch = word[idx]   
    nextLocation = root.children.get(ch)
    nodeDelete = False

    if len(nextLocation.children) > 1:
        delete(nextLocation,word,idx+1)
        return False
    if len(word) == idx+1:
        if len(nextLocation.children) >= 1:
            nextLocation.endSring = False
            return False
        else:
            root.children.pop(ch)
            return True
        
    if nextLocation.endString == True:
        delete(nextLocation,word,idx+1)
        return False
    
    nodeDelete = delete(nextLocation,word,idx+1)
    if nodeDelete == True:
        root.children.pop(ch)
        return True
    else:
        return False



sti = Trie()
print(sti.insert('api'))
print(sti.insert('apple'))
delete(sti.root,'api',0)
print(sti.search('api'))
