# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        
        if list1.val<list2.val:
            res = list1
            list1 = list1.next
        else:
            res = list2
            list2 = list2.next
        dum = res
        while list1 and list2:
            if list1.val>list2.val:
                dum.next=list2
                list2 = list2.next
            else:
                dum.next=list1
                list1 = list1.next
            dum = dum.next
        if list1:
            dum.next = list1
        else:
            dum.next = list2
        return res
        