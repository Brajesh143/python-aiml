class Stack:
    def __init__(self):
        self.items = []

    def push(self, items):
        if items is not None:
            self.items.append(items)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0    


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.items)

print(stack.peek())      # 30
print(stack.pop())       # 30
print(stack.peek())      # 20
print(stack.pop())       # 20
print(stack.pop())       # 10
print(stack.pop())       # None
print(stack.is_empty())