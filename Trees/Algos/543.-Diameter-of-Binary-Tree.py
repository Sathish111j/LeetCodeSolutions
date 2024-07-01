# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0

        def height(node):
            if node is None:
                return 0
            
            left_height=height(node.left)
            right_height=height(node.right)

            dia = left_height+right_height

            self.diameter=max(dia, self.diameter)

            return max(left_height, right_height)+1
        height(root)
        return self.diameter