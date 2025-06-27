# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        if root.val == x or root.val == y:
            return False

        q = deque([(root, None)])
        parent1 = None
        parent2 = None
        depth1 = None
        depth2 = None

        depth = 0

        while q:

            for i in range(len(q)):
                node, parent = q.popleft()

                if node.val == x:
                    parent1 = parent
                    depth1 = depth
                
                elif node.val == y:
                    parent2 = parent
                    depth2 = depth

                if node.left:
                    q.append((node.left, node))
                
                if node.right:
                    q.append((node.right,node))
            depth += 1
        

        return parent1 != parent2 and depth1 == depth2


# there is another solution where we can return early once both x and y are found. (Todo(1))