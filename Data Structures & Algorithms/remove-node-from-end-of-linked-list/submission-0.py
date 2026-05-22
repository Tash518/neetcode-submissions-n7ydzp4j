# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        while(curr):
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        head = prev # reversed now
        
        if n==1:
            head = head.next
        else:
            count = 1
            temp = prev
            while temp and count<n-1:
                temp = temp.next
                count+=1
            temp.next = temp.next.next
        #reverse again
        prev = None
        curr = head
        while(curr):
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        return prev


        