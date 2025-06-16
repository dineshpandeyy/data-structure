# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = deque([(original,cloned)])

        while q:
            org, copy = q.popleft()
            if org == target:
                return copy
            
            if org.left:
                q.append((org.left,copy.left))

            if org.right:
                q.append((org.right,copy.right))
        