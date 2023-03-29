from LL_Skeleton import *

def partition(ll,x):
    tempNode = ll.head
    ll.tail = ll.head

    while tempNode:
        nextNode = tempNode.next
        tempNode.next = None
        if tempNode.data < x:
            tempNode.next = ll.head
            ll.head = tempNode
        else:
            ll.tail.next = tempNode
            ll.tail = tempNode
        tempNode = nextNode
    
    if ll.tail.next is not None:
        ll.tail.next = None

csll = LinkedListBody()
csll.generate(7,2,10)
print(csll)
partition(csll,40)
print(csll)