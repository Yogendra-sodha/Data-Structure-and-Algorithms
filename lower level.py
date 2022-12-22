class demo:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class d2:
    def __init__(self):
        self.head = None
    def debug(self,value):
        a = demo(value)
        a.next = 2
        print("The value of a is",a.data,"next value is",a.next)

aa = d2()
aa.debug(12)