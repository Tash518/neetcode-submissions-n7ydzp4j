# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        prev = None if left==1 else head
        cnt=1
        while prev and prev.next and cnt<left-1:
            prev= prev.next
            cnt+=1
        leftNode = prev.next if prev else head
        cnt=left
        rightNode = leftNode
        while cnt<right:
            rightNode = rightNode.next
            cnt+=1
        prevOfLeft = prev
        cur = leftNode
        stop = rightNode.next
        while cur!=stop:
            nextnode = cur.next
            cur.next = prev
            prev = cur
            cur = nextnode
        leftNode.next = cur
        if prevOfLeft:
            prevOfLeft.next = prev
        else:
            head = prev
        return head
            
            