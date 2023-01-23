from LL_Skeleton import *

def nthpos(ll,n):
    p1 = ll.head
    p2 = ll.head

    for i in range(n):
        if p2 is None:
            return None
        p2 = p2.next

    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1

csll = LinkedListBody()
csll.generate(6,1,20)
print(csll)
print(nthpos(csll,2))