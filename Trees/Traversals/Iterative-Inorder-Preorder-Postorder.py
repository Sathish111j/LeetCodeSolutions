def inorder_traversal(root):
    inorder = []
    stack = []
    node = root
    
    while True:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            if not stack:
                break
            node = stack.pop()
            inorder.append(node.val)
            node = node.right
            
    return inorder

def preorder_traversal(root):
    if root is None:
        return []
    
    preorder = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        preorder.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
            
    return preorder