# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prevofleft = None 
        leftNode = head
        for _ in range(left-1):
            prevofleft,  leftNode = leftNode, leftNode.next
        #reversi r-l+1 times
        prev = None
        cur = leftNode
        for _ in range(right-left+1):
            nextnode = cur.next
            cur.next = prev
            prev = cur
            cur = nextnode
        leftNode.next = cur
        if prevofleft:
            prevofleft.next = prev
        else:
            head = prev
        return head