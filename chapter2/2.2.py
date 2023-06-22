from linkedlist import LinkedListNode, CreateLinkedList, PrintLinkedList

# 1,2,3,4,5 k = 3 / output:3

# def k_node(node, k):
#     curr = node
#     arr = []

#     while curr:
#         arr = curr
#         curr= curr.next

#     result = arr[-k]

#     return result


def k_node(head, k):
    p1 = head # fast
    p2 = head # slow

    for i in range(k):
        if not p1:
            return None
        else:
            p1 = p1.next

    while p1:
        p1 = p1.next
        p2 = p2.next

    return p2



arr = [1,2,3,6,7,8,9]
linkedlist = CreateLinkedList.create_linkedlist(arr)
result_k = k_node(linkedlist, 3)
# PrintLinkedList.print_linkedlist(deleted_list)
print(result_k)


