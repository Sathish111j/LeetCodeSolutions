# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return []
        
        queue=deque([root])

        level=0
        while queue:
            levelSize=len(queue)

            prev=float("-inf") if level%2==0 else float("inf")

            for i in range(levelSize):
                node=queue.popleft()

                if level%2==0:
                    if node.val<=prev or node.val%2==0:
                        return False
                    
                else:
                    if node.val>=prev or node.val%2==1:
                        return False

                prev=node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return True
                
            


