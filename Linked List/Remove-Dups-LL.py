from LL_Skeleton import LinkedListBody

def removeDups(ll):
    if ll.head is None:
        return

    else:
        temp = ll.head
        uniSet = []
        while temp.next:
            if temp.next.data in uniSet:
                temp.next = temp.next.next
            else:
                uniSet.append(temp.data)
                temp = temp.next
        return ll

# Call class from linkedlist py file the body that was created

customLL = LinkedListBody()
customLL.generate(5,3,6)
print(customLL)
removeDups(customLL)
print(customLL)