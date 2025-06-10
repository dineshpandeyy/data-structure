# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNodes(head):
    stack = []

    curr = head
    while curr:
        if not stack:
            stack.append(curr.val)
        else:
            while stack and stack[-1] < curr.val:
                stack.pop()
            stack.append(curr.val)
        curr = curr.next
    
    node = ListNode(-1)
    dummy = node

    for val in stack:
        npt = ListNode(val)
        node.next = npt
        node = node.next
    
    return dummy.next