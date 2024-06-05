# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        columns=defaultdict(list)
        min_col=max_col=0

        queue=deque([(root,0,0)])

        while queue:
            node ,row,col=queue.popleft()

            if node is not None:

                 # track the min and max column indices
                min_col = min(min_col, col)
                max_col = max(max_col, col)

                columns[col].append((row,node.val))
                queue.append((node.left,row+1,col-1))
                queue.append((node.right,row+1,col+1))

        result=[]

        for col in range(min_col,max_col+1):
            #sorting by row then value
            columns[col].sort(key=lambda x:(x[0],x[1]))
            result.append([val for row ,val in columns[col]])

        return result
