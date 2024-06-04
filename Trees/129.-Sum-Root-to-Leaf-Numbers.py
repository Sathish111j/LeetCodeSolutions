# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def helper(root,totalSum):
            if root is None:
                return 0
            
            totalSum =totalSum *10 +root.val
            if root.left is None and  root.right is None:
                return totalSum 
            left = helper(root.left, totalSum)
            right=helper(root.right, totalSum)
            
            return left +right
        
        return helper(root,0)
        
        