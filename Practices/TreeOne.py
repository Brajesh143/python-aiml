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

root.right.left = Node(12)
root.right.right = Node(20)   


def inorder(root):
    if root is None:
        return

    inorder(root.left)

    print(root.value, end=" ")

    inorder(root.right)


inorder(root)

def preorder(root):
    if root is None:
        return

    print(root.value, end=" ")

    preorder(root.left)

    preorder(root.right)


preorder(root)

def postorder(root):
    if root is None:
        return

    postorder(root.left)

    postorder(root.right)

    print(root.value, end=" ")

postorder(root)