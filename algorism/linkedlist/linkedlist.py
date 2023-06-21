class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None
        pass


# LinkedListの作成
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        pass

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.prev = curr_node
       

    def delete(self, value):
        curr_node = self.head

        while curr_node is not None:
            if curr_node.value == value:# 現在のnodeが削除すう引数のvalueかどうか
                if curr_node.prev is not None:
                    curr_node.prev.next = curr_node.next
                else:
                    self.head = curr_node.next
                if curr_node.next is not None:
                    curr_node.next.prev = curr_node.prev
                return
            curr_node = curr_node.next
        print("Value not found in the list.")



    def output(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.value)
            curr_node = curr_node.next
        print()

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(5)
print('linkedlist : ')
l.output()
print('linkedlist delete ... 5 : ')
l.delete(5)
l.output()