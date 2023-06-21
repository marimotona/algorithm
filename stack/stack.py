class Stack:
    def __init__(self) -> None:
        self.array = []
        pass

    def add(self, value):
        # array = []
        self.array.insert(0, value)
        

    def pop(self):
        if len(self.array) > 0:
            self.array = self.array[1:]
            return self.array
    
    def __str__(self):
        return str(self.array)

    
a = Stack()
print('stack add : ')
a.add(1)
a.add(2)
a.add(3)
a.add(8)
print(a)
print('stack pop : ')
a.pop()
a.pop()
print(a)