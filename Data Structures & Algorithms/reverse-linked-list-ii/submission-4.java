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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode prevofleft = null;
        ListNode leftnode = head;
        for(int i = 0;i<left-1;i++){
            prevofleft = leftnode;
            leftnode = leftnode.next;
        }
        ListNode prev = null;
        ListNode cur = leftnode;
        for(int i=0;i<right-left+1;i++){
            ListNode nextnode = cur.next;
            cur.next = prev;
            prev = cur;
            cur = nextnode;
        }
        leftnode.next = cur;
        if(prevofleft!=null){
            prevofleft.next = prev;
        }else{
            head = prev;
        }
        return head;
    }
}