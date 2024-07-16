# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def lowestCommonAncestor(self,root,p,q):
        if root is  None:
            return None
        if root.val==q or root.val ==p:
            return root

        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)

        if left is not None and right is not None:
            return root
        
        if left is not None :
            return left
        else:
            return right
        
    def findPath(self,lca,target,path):
        if lca is None :
            return None
        
        if lca.val==target:
            return True
        
        path.append("L")

        if self.findPath(lca.left,target,path):
            return True
        path.pop()
        
        path.append("R")

        if self.findPath(lca.right,target,path):
            return True
        
        path.pop()
        
        return False

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lca=self.lowestCommonAncestor(root,startValue,destValue)

        pathFromstart=[]

        self.findPath(lca,startValue,pathFromstart)

        pathFromDest=[]

        self.findPath(lca,destValue,pathFromDest)

        return "U"*len(pathFromstart) + "".join(pathFromDest)
        