# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.val>key:
           root.left= self.deleteNode(root.left,key)
        elif root.val<key:
           root.right=self.deleteNode(root.right,key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            #finding inorder sucessor

            sucessor=self.findInorderSucessor(root.right)
            root.val=sucessor.val

            root.right=self.deleteNode(root.right,sucessor.val)
        return root


    def findInorderSucessor(self,node):
        current=node
        while current.left is not None:
            current=current.left
        return current