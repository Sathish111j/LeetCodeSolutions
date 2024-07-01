def inorder_traversal(root):
    result = []
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
            result.append(node.val)
            node = node.right
            
    return result

def preorder_traversal(root):
    if root is None:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
            
    return result

def postorder_traversal(root):
    if root is None:
        return []
    
    st1 = []
    st2 = []
    result = []
    
    st1.append(root)
    while st1:
        node = st1.pop()
        st2.append(node)
        if node.left is not None:
            st1.append(node.left)
        if node.right is not None:
            st1.append(node.right)
    
    while st2:
        node = st2.pop()
        result.append(node.val)
    
    return result

def postorder_traversal(root): # Using one stack
    if not root:
        return []

    stack = []
    post = []
    cur = root
    
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        
        temp = stack[-1].right
        if not temp:
            temp = stack.pop()
            post.append(temp.val)
            while stack and temp == stack[-1].right:
                temp = stack.pop()
                post.append(temp.val)
        else:
            cur = temp
    
    return post

def all_traversals(root):
    if not root:
        return [], [], []

    stack = [(root, 1)]
    preorder = []
    inorder = []
    postorder = []

    while stack:
        node, state = stack.pop()

        if state == 1:
            # Preorder: Add node to preorder list, push node with state 2, then left child with state 1
            preorder.append(node.val)
            stack.append((node, 2))
            if node.left:
                stack.append((node.left, 1))
        elif state == 2:
            # Inorder: Add node to inorder list, push node with state 3, then right child with state 1
            inorder.append(node.val)
            stack.append((node, 3))
            if node.right:
                stack.append((node.right, 1))
        else:
            # Postorder: Add node to postorder list
            postorder.append(node.val)

    return preorder, inorder, postorder
