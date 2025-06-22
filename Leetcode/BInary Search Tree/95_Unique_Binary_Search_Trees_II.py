# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return [None]

        def solve(start,end):
            if start > end:
                return [None]

            res = []        
            for i in range(start,end+1):
                leftSubTrees = solve(start, i-1)
                rightSubTrees = solve(i+1,end)

                for left in leftSubTrees:
                    for right in rightSubTrees:
                        root = TreeNode(i,left,right)
                        res.append(root)

            return res
        
        return solve(1,n)
        


        