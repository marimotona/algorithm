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

# node1 = LinkedListNode(1)
# node2 = LinkedListNode(2)
# node3 = LinkedListNode(3)
# node4 = LinkedListNode(2)

# # ノードを連結
# node1.next = node2
# node2.next = node3
# node3.next = node4


# def print_linked_list(node):
#     curr = node
#     while curr:
#         print(curr.value, end=" ")
#         curr = curr.next
#     print()

arr = [1,2,3,2]
lenkedlist = CreateLinkedList.create_linkedlist(arr)
deleted_list = delete_list(lenkedlist)
PrintLinkedList.print_linkedlist(deleted_list)