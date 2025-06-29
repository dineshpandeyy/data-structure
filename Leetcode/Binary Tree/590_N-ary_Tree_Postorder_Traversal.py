"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        res = []

        def solve(root):
            if not root:
                return 
            for pt in root.children:
                solve(pt)
            
            res.append(root.val)
        solve(root)
        return res
        