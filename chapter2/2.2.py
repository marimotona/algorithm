from linkedlist import LinkedListNode, CreateLinkedList, PrintLinkedList

# 1,2,3,4,5 k = 3 / output:3



node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node4 = LinkedListNode(2)

# ノードを連結
node1.next = node2
node2.next = node3
node3.next = node4


def print_linked_list(node):
    curr = node
    while curr:
        print(curr.value, end=" ")
        curr = curr.next
    print()




