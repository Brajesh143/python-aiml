class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# create linkedlist 10 → 20 → 30 → 40 → NULL

def print_list(head):
    current = head

    while current:
        print(current.value, end=" → ")
        current = current.next
        
    print("NULL")

def traversed_list(head):
    current = head

    while current:
        print(current.value)
        current = current.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print_list(head)
traversed_list(head)