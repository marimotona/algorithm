from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        pass


# 帰りがけ順
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end='')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

#postorder(root)


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end='')
        inorder(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# inorder(root)

def preorder(node):
    if node is not None:
        print(node.data, end='')
        preorder(node.left)
        preorder(node.right)

    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# preorder(root)


# bfs
class Queue:
    def __init__(self) -> None:
        self.queue = deque()

    def enqueue(self, node):
        # インスタンスのキューにノードを追加
        self.queue.append(node)

    def dequeue(self):
        # popleft() 先頭から削除
        return self.queue.popleft()

    def is_empty(self):
            return len(self.queue) == 0
    
def bfs(root):
    if root is None:
        return
    queue = Queue()
    queue.enqueue(root)

    while not queue.is_empty():
        node = queue.dequeue()
        print(node.data, end=" ")
        if node.left is not None:
            queue.enqueue(node.left)
        if node.right is not None:
            queue.enqueue(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# bfs(root)

def dfs(node):
    if root is None:
        return
    stack = []
    stack.append(node)
    while stack:
        node = stack.pop()
        print(node.data, end=" ")
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

dfs(root)