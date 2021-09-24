class Node:
    def __init__(self, value=None, left=None, right=None):

        self.value = value

        if left is not None and not isinstance(left, Node):
            raise TypeError(f"Expected: {Node} but Found: {type(left)}")
        if right is not None and not isinstance(right, Node):
            raise TypeError(f"Expected: {Node} but Found: {type(right)}")

        self.left = left
        self.right = right

    def add_left(self, left):
        if self.left is None:
            self.left = left
        else:
            raise Exception("This tree already has a left child.")

    def add_right(self, right):
        if self.right is None:
            self.right = right
        else:
            raise Exception("This tree already has a right child.")

    def get_value(self):
        return self.value

    def is_leaf(self):

        if self.left is None and self.right is None:
            return True
        else:
            return False

    def postorder(self, res):
        if self.left is not None:
           self.left.postorder(res)
        if self.right is not None:
            self.right.postorder(res)

        res.append(self.get_value())

        return res

def inorder(node):
    if node is None:
        return 0

    else:
        inorder(node.left)
        print(node.get_value())
        inorder(node.right)


def preorder(node):
    if node is None:
        return 0
    else:
        print(node.get_value())
        preorder(node.left)
        preorder(node.right)
