# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root):

        ls = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            ls.append(root.val)
            inorder(root.right)
        
        inorder(root)

        root = TreeNode(ls[0])
        dummy = root

        for i in range(1, len(ls)):
            node = TreeNode(ls[i])
            root.right = node
            root = root.right
        
        return dummy


        