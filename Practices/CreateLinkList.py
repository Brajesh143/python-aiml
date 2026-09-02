class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(head):
    current = head

    while current:
        print(current.value, end=" → ")
        current = current.next

    print("NULL")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print_list(head)