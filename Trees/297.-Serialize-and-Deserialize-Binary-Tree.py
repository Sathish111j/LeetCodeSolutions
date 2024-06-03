# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "null"
        
        left_serialized = self.serialize(root.left)
        right_serialized = self.serialize(root.right)
        
        return str(root.val) + "," + left_serialized + "," + right_serialized

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(queue):
            val = queue.pop(0)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = helper(queue)
            node.right = helper(queue)
            return node
        
        queue = data.split(",")
        return helper(queue)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))