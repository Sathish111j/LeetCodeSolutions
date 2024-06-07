# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # def findnode(root,val):
        #     if root is None:
        #         return None
            
        #     left =findnode(root.left,val)

        #     if root.val==val:
        #         return root

        #     if left is not None :
        #         return left

        #     return findnode(root.right,val)
        
        def same(root,subroot):
            if root is None and subroot is None:
                return True
            if root is None or subroot is None:
                return False
            
            if root.val!= subroot.val:
                return False
            
            return same(root.left,subroot.left) and same(root.right,subroot.right)
        
        def helper(root,subRoot):
            if root is None:
                return False
            if same(root,subRoot):
                return True
            return helper(root.left,subRoot) or helper(root.right,subRoot) 
        
        return helper(root,subRoot)
