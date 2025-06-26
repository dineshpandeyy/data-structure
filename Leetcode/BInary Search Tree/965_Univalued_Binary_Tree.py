# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root) -> bool:
        ls = set()
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            ls.add(root.val)
            inorder(root.right)
        
        inorder(root)
        return len(ls) == 1
        