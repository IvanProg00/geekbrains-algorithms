class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return f"[{self.val}] => {self.next}"


class List:
    def __init__(self):
        self.head = None

    def push(self, val):
        node = Node(val)
        node.set_next(self.head)
        self.head = node

    def pop(self):
        if self.head is None:
            return

        node = self.head
        self.head = self.head.get_next()
        return node

    def reverse(self):
        cur = self.head
        if cur is None:
            return
        next = cur.get_next()
        cur.set_next(None)

        while next is not None:
            next_next = next.get_next()
            next.set_next(cur)
            cur, next = next, next_next

        self.head = cur

    def __repr__(self) -> str:
        return str(self.head)


data = List()
data.push(2)
data.push(4)
data.push(6)
data.push(8)
data.push(10)
data.push(12)
data.push(14)

# Reverse
print(data)
data.reverse()
print(data)

print(data.pop().val)
print(data)
print(data.pop().val)
print(data)
