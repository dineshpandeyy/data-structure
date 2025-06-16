# Definition for a binary tree node.
'''
Given two binary search trees root1 and root2, return a list containing 
all the integers from both trees sorted in ascending order.
Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:

        res = []
        def inorder(root1):
            if not root1:
                return 
            inorder(root1.left)
            res.append(root1.val)
            inorder(root1.right)
        
        inorder(root1)
        inorder(root2)
        res.sort()
        return res