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

# alternate method

def remove_with_loop(ll):
    temp = ll.head
    while temp:
        runner = temp
        while runner.next: #1334
            if runner.next.data == temp.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        temp = temp.next
    return ll.head
    



# Call class from linkedlist py file the body that was created

customLL = LinkedListBody()
# Then generating linked list by using method created in ll body.py file
customLL.generate(5,3,6)
print(customLL)
# Using the function to remove the duplicate from generated linked list
remove_with_loop(customLL)
print(customLL)