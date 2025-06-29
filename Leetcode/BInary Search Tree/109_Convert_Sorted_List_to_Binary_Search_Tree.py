# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next

        def buildTree(arr):
            if not arr:
                return 
            
            middle = len(arr) // 2
            root = TreeNode(arr[middle])
            root.left = buildTree(arr[:middle])
            root.right = buildTree(arr[middle+1:])
            return root
        
        return buildTree(nums)
        