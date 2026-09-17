class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(head):
    current = head

    while current:
        print(current.value, end=" -> ")
        current = current.next

    print("NULL")


def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev

        prev = current
        current = next_node

    return prev


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Before:")
print_list(head)

head = reverse_linked_list(head)

print("After:")
print_list(head)