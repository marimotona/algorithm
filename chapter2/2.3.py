from linkedlist import LinkedListNode, CreateLinkedList, PrintLinkedList

# 1,5,7,9 / 7 -> 1,5,9

def delete(node):
    # node.value = node.next.value
    # node.next = node.next.next

    # return node
    if node is None or node.next is None:
        return False
    
    next_node = node.next
    node.value = next_node.value
    node.next = next_node.next

    return True

arr = [1,5,7,9] # 7
linkedlist = CreateLinkedList.create_linkedlist(arr)
node_delete = linkedlist.next.next
deleted_list = delete(node_delete)
PrintLinkedList.print_linkedlist(linkedlist)
# print(deleted_list)