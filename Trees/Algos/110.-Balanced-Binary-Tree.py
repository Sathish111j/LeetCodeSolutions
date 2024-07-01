# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root is None:
                return 0 ,True
            
            leftHeight ,isLeftBalanced =helper(root.left)
            rightHeight ,isRightBalanced =helper(root.right)

            return max(leftHeight,rightHeight)+1 ,isLeftBalanced and isRightBalanced and abs(leftHeight - rightHeight) <= 1
        
        height,result=helper(root)
        return result
        

        
    