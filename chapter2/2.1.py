from linkedlist import LinkedListNode, CreateLinkedList, PrintLinkedList


def delete_list(node):
    curr = node
    prev = None
    seen = set()

    while curr:
        if curr.value in seen:
            prev.next = curr.next
        else:
            seen.add(curr.value)
            prev = curr
        curr = curr.next

    return node


arr = [1,2,3,2]
linkedlist = CreateLinkedList.create_linkedlist(arr)
deleted_list = delete_list(linkedlist)
PrintLinkedList.print_linkedlist(deleted_list)