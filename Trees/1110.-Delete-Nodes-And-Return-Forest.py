# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        toDelete=set(to_delete)

        forest=[]

        def dfs(node,root):
            if not node:
                return None
            
            isToBeDeleted=node.val in toDelete

            if root and not isToBeDeleted:
                forest.append(node)
            
            node.left=dfs(node.left,isToBeDeleted)
            node.right=dfs(node.right,isToBeDeleted)

            if isToBeDeleted:
                return None
            else:
                return node
        dfs(root,True)

        return forest

