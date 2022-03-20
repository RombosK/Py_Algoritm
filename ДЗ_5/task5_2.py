# Проверить дерево на симметричность: https://leetcode.com/problems/symmetric-tree/
# 1
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root: Optional[TreeNode]) -> bool:

    def tree(left, right):
        if left == None:
            return right == None
        elif right == None:
            return left == None
        elif left.val != right.val:
            return False
        else:
            return tree(left.left, right.right) and tree(left.right, right.left)

    if root == None:
        return True
    else:
        return tree(root.left, root.right)


class Solution:
    pass

# 2

# from typing import Optional
#
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         def mirror(left, right):
#             if not left and not right:
#                 return True
#             if not left or not right:
#                 return False
#             return left.val == right.val and mirror(left.left, right.right) and mirror(left.right, right.left)
#
#         return mirror(root, root)
