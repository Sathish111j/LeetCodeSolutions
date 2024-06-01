# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_node(self, node, x):
        if node is None:
            return None
        if node.val == x:
            return node
        left = self.find_node(node.left, x)
        if left is not None:
            return left
        return self.find_node(node.right, x)

    def isSibling(self, node, x, y):
        if node is None:
            return False
        return ((node.left and node.right) and ((node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x)) or self.isSibling(node.left, x, y) or self.isSibling(node.right, x, y))

    def level(self, node, x, lev):
        if node is None:
            return 0
        if node.val == x:
            return lev
        downlevel = self.level(node.left, x, lev + 1)
        if downlevel != 0:
            return downlevel
        return self.level(node.right, x, lev + 1)

    def isCousins(self, root, x, y):
        if root is None:
            return False
        return (self.level(root, x, 0) == self.level(root, y, 0)) and not self.isSibling(root, x, y)