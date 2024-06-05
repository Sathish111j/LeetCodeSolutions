# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     if not inorder or not preorder:
    #         return None
        
    #     root_val=preorder.pop(0)
    #     root =TreeNode(root_val)
    #     root_index=inorder.index(root_val)

    #     root.left=self.buildTree(preorder,inorder[:root_index])
    #     root.right=self.buildTree(preorder,inorder[root_index+1:])
    #     return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None

       
            root_val = preorder[preorder_left]
            root = TreeNode(root_val)

            
            root_index = inorder_index_map[root_val]

          
            left_subtree_size = root_index - inorder_left

          
            root.left = helper(preorder_left + 1, preorder_left + left_subtree_size,
                               inorder_left, root_index - 1)
            root.right = helper(preorder_left + left_subtree_size + 1, preorder_right,
                                root_index + 1, inorder_right)

            return root

   
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
