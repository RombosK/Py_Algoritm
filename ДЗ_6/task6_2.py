# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


tree = Node(1)
tree.left = Node(2)
tree.left.next = tree.right
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.left.left.next = tree.left.right
tree.right = Node(3)
tree.right.right = Node(7)
tree.left.right.next = tree.right.right


def connect(root):
    if root is None or root.right is None:
        return root

    dq = deque()
    dq.append(root)

    while dq:
        size = len(dq)
        for el in range(size):
            curr = dq.popleft()
            if el != size - 1:
                curr.next = dq[0]
            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)
    return root
