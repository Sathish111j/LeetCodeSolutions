# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        elem={}

        def helper(root):
            if root is None :
                return False
            if   k -  root.val in elem:
                return True
            else:
                elem[root.val]=root.val
            
            left=helper(root.left)
            right=helper(root.right)

            return left or right

        return helper(root)
        