class SetOfStacks:
    def __init__(self, capacity) -> None:
        self.stacks = [[]]
        self.capacity = capacity
        pass

    # stacksは、stackの集まり
    # self.stacks[-1]は、スタックのリストの最後のスタックを指す
    # たくさんあるスタックの中のことを指している
    def push(self, val):
        # 最新のstackの大きさを比較している
        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(val)

    def pop(self):
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if not self.stacks:
            return None
        val = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return val