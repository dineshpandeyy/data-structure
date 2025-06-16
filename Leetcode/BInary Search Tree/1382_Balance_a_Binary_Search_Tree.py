# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root):
            ls = []
            def inorder(root):
                if not root:
                    return 
                inorder(root.left)
                ls.append(root)
                inorder(root.right)
            
            inorder(root)

            def solve(arr):
                if not arr:
                    return 
                
                mid = (len(arr)) // 2
                root = arr[mid]

                root.left = solve(arr[:mid])
                root.right = solve(arr[mid+1:])
                return root
            
            return solve(ls)