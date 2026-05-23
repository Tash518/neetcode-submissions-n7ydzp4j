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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode nextnode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextnode;
        }

        head = prev;

        if (n == 1) {
            head = head.next;
        }else{
            int count = 1;
            ListNode temp = prev;
            while( temp!=null && count<n-1){
                temp = temp.next;
                count++;
            }
            temp.next = temp.next.next;
        }
        prev = null;
        curr = head;
        while(curr!=null){
            ListNode nextnode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextnode;
        }
        return prev;
    }
}
