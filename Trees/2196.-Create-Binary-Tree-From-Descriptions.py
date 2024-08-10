# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # mp = {}
        # hasParent = set()

        # for desc in descriptions:
        #     if desc[0] not in mp:
        #         mp[desc[0]] = TreeNode(desc[0])
        #     if desc[1] not in mp:
        #         mp[desc[1]] = TreeNode(desc[1])
        #     hasParent.add(desc[1])

        # root = None
        # for desc in descriptions:
        #     if desc[2] == 1:  # left
        #         mp[desc[0]].left = mp[desc[1]]
        #     else:  # right
        #         mp[desc[0]].right = mp[desc[1]]
        #     if desc[0] not in hasParent:
        #         root = mp[desc[0]]

        # return root

        map1 = {n: TreeNode(n) for _, n, _ in descriptions}
        root = None
        for p, c, d in descriptions:
            if p not in map1:
                root=map1[p] = TreeNode(p)
            if d == 1:
                map1[p].left = map1[c]
            else:
                map1[p].right = map1[c]
        return root