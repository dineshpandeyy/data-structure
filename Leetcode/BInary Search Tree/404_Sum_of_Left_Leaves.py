# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        value = 0

        while q:
            node = q.popleft()
            if node.left:
                if not node.left.left and not node.left.right:
                    value += node.left.val
                else:
                    q.append(node.left)
            if node.right:
                q.append(node.right)

        return value        