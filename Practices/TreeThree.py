class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)

def search_bst(root, target):

    if root is None:
        return False

    if target == root.value:
        return True

    if target < root.value:
        return search_bst(root.left, target)

    return search_bst(root.right, target)

print(search_bst(root, 7))
print(search_bst(root, 12))