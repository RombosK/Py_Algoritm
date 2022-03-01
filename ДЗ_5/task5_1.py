# Реализовать обход дерева post-order. Сначала левое, потом правое поддерево, в последнюю очередь корень:
# https://leetcode.com/problems/binary-tree-postorder-traversal/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.left = TreeNode(3)
tree.left.left = TreeNode(4)


class Solution(object):
    def postorderTraversal(root):
        res = []

        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)
                res.append(node.val)

        helper(root)
        return res


postorder = Solution.postorderTraversal(tree)
print(postorder)
