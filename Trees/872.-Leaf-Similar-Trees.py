# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafs(node):
            if node is None:
                return []
            
            if node and node.left is None and node.right is None:
                return [node.val]

            left=leafs(node.left)
            right=leafs(node.right)

            return left +right

        if root1 is None and root2 is None:
            return True
        if leafs(root1)==leafs(root2):
            return True
        else:
            return False

