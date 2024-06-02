# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        queue=deque([root])
        
        while queue:
            level_size=len(queue)
            level=[]

            for _ in range(level_size):
                node=queue.popleft()

                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level.append(None)
            
            if level != level[::-1]:
                return False
            
        return True
        