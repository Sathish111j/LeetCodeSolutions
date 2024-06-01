# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue=deque([root])
        result=[]
        count=0
        
        while queue:
            level_size=len(queue)
            level_queue=deque()
            

            for _ in range(level_size):
                node=queue.popleft()
                

                if count%2 ==0:
                    level_queue.append(node.val)
                else:
                    level_queue.appendleft(node.val)
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
    
                
            result.append(level_queue)
            count+=1

        return result
