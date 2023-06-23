from linkedlist import LinkedListNode, CreateLinkedList, PrintLinkedList

def cycle_list(node):
    slow = node
    fast = node

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return slow.value
        
    return None


# cycle_node = CreateLinkedList.create_linkedlist([7, 1, 6, 5, 2, 6, 5, 2, 6])

# Create nodes
node1 = LinkedListNode(7)
node2 = LinkedListNode(1)
node3 = LinkedListNode(6)
node4 = LinkedListNode(5)
node5 = LinkedListNode(2)
node6 = LinkedListNode(6)

# Connect nodes to create a linked list
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

# Create a cycle by connecting the last node to one of the earlier nodes
node6.next = node4

result = cycle_list(node1)
# PrintLinkedList.print_linkedlist(result)
print(result)