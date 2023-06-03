BLACK = 0
RED = 1


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.color = RED

    def add(self, val):
        if self.val < val:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.add(val)
        else:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.add(val)

    def find(self, val):
        if self.val == val:
            return self

        if self.val < val:
            if self.right is None:
                return None
            return self.right.find(val)
        else:
            if self.left is None:
                return None
            return self.left.find(val)

    def __repr__(self) -> str:
        return f"{self.val}(color: {self.color})\n->[left: {self.left}]\n->[right: \
{self.right}]"


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        self.root = self.insert(self.root, val)
        self.root.color = BLACK

    def insert(self, node, val):
        if node is None:
            return Node(val)

        if val == self.root.val:
            node.val = val
        elif val < self.root.val:
            node.left = self.insert(node.left, val)
        else:
            node.right = self.insert(node.right, val)

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)

        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)

        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_color(node)

        return node

    # TODO: change to one line
    def is_red(self, node):
        if node is None:
            return False
        return node.color == RED

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        new_root.color = node.color
        node.color = RED

        return new_root

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        new_root.color = node.color
        node.color = RED

        return new_root

    def flip_color(self, node):
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK

    def find(self, val):
        if self.root is None:
            return None
        return self.root.find(val)

    def __repr__(self) -> str:
        return self.root.__repr__()


b = BinaryTree()
b.add(1)
b.add(2)
b.add(3)
b.add(7)
b.add(8)
print(b)
