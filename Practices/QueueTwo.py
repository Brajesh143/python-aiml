from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.items:
            return None

        return self.items.popleft()

    def front(self):
        if not self.items:
            return None

        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.front())      # 10
print(queue.dequeue())    # 10
print(queue.dequeue())    # 20
print(queue.is_empty())   # False