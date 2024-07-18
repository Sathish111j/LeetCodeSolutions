# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.goodPairs=0
        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]
            
            leftDistances=dfs(node.left)
            rightDistances=dfs(node.right)

            for left in leftDistances:
                for right in rightDistances:
                    if left + right <=distance:
                        self.goodPairs+=1
            
            CurrentgoodDistances=[]

            for  d in leftDistances +rightDistances :
                if d+1<distance:
                    CurrentgoodDistances.append(d+1)
            
            return CurrentgoodDistances
        
        dfs(root)
        return self.goodPairs
            