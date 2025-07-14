# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        length = 0

        curr = head
        while curr.next:
            length += 1
            curr = curr.next
        
        res = 0
        curr = head
        while curr:
            res += curr.val * 2**length
            length -= 1
            curr = curr.next
        
        return res