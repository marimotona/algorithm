from linkedlist import LinkedListNode, CreateLinkedList, PrintLinkedList

def is_anagram(node):
    # clone = LinkedListNode(node.value)
    reversed = reverse(node)
    return equal(node, reversed)


def reverse(node):
    # prev = None
    # curr = node

    # while curr:
    #     next_node = curr.next
    #     curr.next = prev
    #     prev = curr
    #     curr = next_node

    # return prev

    head = None
    while node:
        n = LinkedListNode(node.value)
        n.next = head
        head = n
        node = node.next
    
    return head # 先頭

def equal(one, two):
    while one and two:
        if one.value != two.value:
            return False
        one = one.next
        two = two.next
    return one is None and two is None

anagram_list = CreateLinkedList.create_linkedlist([7, 1, 6, 5, 6, 1, 7])
result = is_anagram(anagram_list)
# PrintLinkedList.print_linkedlist(result)
print(result)
