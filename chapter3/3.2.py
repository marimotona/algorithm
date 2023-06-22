class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []
        pass

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            remove = self.stack.pop()
            if remove == self.min_stack[-1]:
                self.min_stack.pop()

            # min_stack内の最小の要素と比較をすることで、stack内の最小の要素を確認している
            return remove
        
    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        

