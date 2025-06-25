# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        result = [0]
        def solve(grandparent,parent):
            if not parent:
                return 0
            
            if grandparent.val % 2 == 0:
                if parent.left:
                    result[0] += parent.left.val
                if parent.right:
                    result[0] += parent.right.val
            
            solve(parent,parent.left)
            solve(parent,parent.right)
        
        solve(root,root.left)
        solve(root,root.right)

        return result[0]
        



            

        