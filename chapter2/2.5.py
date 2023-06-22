from linkedlist import LinkedListNode, CreateLinkedList, PrintLinkedList

def sum_list(list1, list2):
    sum_val = change_num(list1) + change_num(list2)
    sum_val =str(sum_val)

    result_head = LinkedListNode(sum_val[-1])
    curr_node = result_head

    for i in range(len(sum_val) - 2, -1, -1):
        new_node = LinkedListNode(sum_val[i])
        curr_node.next = new_node
        curr_node = new_node

    return result_head



def change_num(head):
    node = head
    result = []

    while node:
        result.append(str(node.value))
        node = node.next

    return int(''.join(result[::-1]))


list1 = CreateLinkedList.create_linkedlist([7, 1, 6])
list2 = CreateLinkedList.create_linkedlist([5, 9, 2])
result = sum_list(list1, list2)
PrintLinkedList.print_linkedlist(result)
