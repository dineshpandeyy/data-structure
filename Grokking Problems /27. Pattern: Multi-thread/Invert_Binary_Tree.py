#DFS approach
def invertTree(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: Optional[TreeNode]
    """
    #Normal DFS (any one will work either pre, post or in)
    def dfs(root):
        if not root:
            return 
        dfs(root.left)
        dfs(root.right)
        root.left, root.right = root.right, root.left
    dfs(root)
    return root

#BFS approach
from collections import deque
def invertTree(self, root):
        if not root:
            return None
        
        q = deque([root])
        
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left  # Swap children
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return root
