class TreeNode():
    def __init__(self,data,children=[]):
        self.data = data
        self.children = children

    def __str__(self,level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in (self.children):
            ret += child.__str__(level+1) # child is element from for loop
        return ret                        # .__str__(level=0,1,2) will call the str method of level given
    
    def addChild(self,child):
        self.children.append(child)
        return self.children
        
    def __repr__(self):
        return str(self.children)

drinks = TreeNode("drink",[])
cold = TreeNode("cold",[])
hot = TreeNode("hot",[])
drinks.addChild(cold)
drinks.addChild(hot)
tea = TreeNode("tea",[])
coffee = TreeNode("coffee",[])
hot.addChild(tea)
hot.addChild(coffee)
cola = TreeNode("cola",[])
fanta = TreeNode("fanta",[])
cold.addChild(cola)
cold.addChild(fanta)
print(drinks)