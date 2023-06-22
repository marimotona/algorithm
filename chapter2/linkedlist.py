class LinkedListNode:
    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self) -> str:
        return str(self.value)
    

class CreateLinkedList:
    # @staticmethod
    def create_linkedlist(arr):
        if not arr:
            return None
        
        head = LinkedListNode(arr[0])
        curr = head

        for i in range(1, len(arr)):
            new_node = LinkedListNode(arr[i])
            curr.next = new_node
            curr = new_node

        return head
    
class PrintLinkedList:
    # @staticmethod
    def print_linkedlist(head):
        curr = head
        while curr:
            print(curr.value, end=" ")
            curr = curr.next
        print()