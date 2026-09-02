class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

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
head.next.next.next.next.next = Node(6)

print_list(head)

middle = find_middle(head)

print(middle.value)