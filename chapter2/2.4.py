# 3,5,8,5,10,2,1 / 5
# 3,1,2,10,5,5,8

# 1,9,4,6,8,6 /x = 4
# 1,4,6,8,6,9

from linkedlist import LinkedListNode, CreateLinkedList, PrintLinkedList

# def pivot_node(pivot, head):
#     search_node = head
#     prev = None
#     curr_left = pivot.value
#     curr_right = pivot.value


#     while search_node:
#         if search_node.value < pivot.value: # pivotのleft
#             pivot.prev = search_node.value
#             pivot.prev = curr_left
#         else:
#             pivot.next = search_node.value # 4,9
#             pivot.next = curr_right

#     return head

def pivot_node(node, x):
    head = node
    tail = node

    while node:
        next_node = node.next
        if node.value < x:
            node.next = head # pivot = 6 / node = 4
            head = node
        else:
            tail.next = node
            tail = node
        
        node = next_node

    tail.next = None

    return head


arr = [1,9,4,6,8,6]
linkedlist = CreateLinkedList.create_linkedlist(arr)
pivot = 4
pivot_list = pivot_node(linkedlist, pivot)
PrintLinkedList.print_linkedlist(pivot_list)