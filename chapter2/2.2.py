from linkedlist import LinkedListNode, CreateLinkedList, PrintLinkedList

# 1,2,3,4,5 k = 3 / output:3

def k_node(node, k):
    curr = node
    arr = []

    while curr:
        arr = curr
        curr= curr.next

    result = arr[-k]

    return result



node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node4 = LinkedListNode(6)
node5 = LinkedListNode(7)

# ノードを連結
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


def print_linked_list(node):
    curr = node
    while curr:
        print(curr.value, end=" ")
        curr = curr.next
    print()

result_list = k_node(node1, 2)
print_linked_list(result_list)


