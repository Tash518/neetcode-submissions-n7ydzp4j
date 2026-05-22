/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null)
            return list2;
        if (list2 == null)
            return list1;
        ListNode res;
        if (list1.val < list2.val) {
            res = list1;
            list1 = list1.next;
        } else {
            res = list2;
            list2 = list2.next;
        }
        ListNode dum = res;
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                dum.next = list1;
                list1 = list1.next;
            } else {
                dum.next = list2;
                list2 = list2.next;
            }
            dum = dum.next;
        }
        if (list1 != null) {
            dum.next = list1;
        }
        if (list2 != null) {
            dum.next = list2;
        }
        return res;
    }
}
