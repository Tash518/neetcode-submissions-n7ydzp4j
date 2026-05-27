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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int v1 = l1 != null ? l1.val : 0;
        int v2 = l2 != null ? l2.val : 0;
        int carry = 0;
        int total = v1 + v2 + carry;
        ListNode head = new ListNode(total % 10);
        carry = total / 10;
        ListNode cur = head;
        l1 = l1 != null ? l1.next : l1;
        l2 = l2 != null ? l2.next : l2;
        while (l1 != null || l2 != null || carry != 0) {
            v1 = l1 != null ? l1.val : 0;
            v2 = l2 != null ? l2.val : 0;
            total = v1 + v2 + carry;
            cur.next = new ListNode(total % 10);
            carry = total / 10;
            l1 = l1 != null ? l1.next : l1;
            l2 = l2 != null ? l2.next : l2;
            cur = cur.next;
        }
        return head;
    }
}
