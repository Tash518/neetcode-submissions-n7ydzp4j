/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if(head==null) return null;
        HashMap<Node, Node> randmap = new HashMap<>();
        Node curr = new Node(head.val);
        randmap.put(head, curr);

        Node ans = curr;

        head = head.next;
        while(head!=null){
            curr.next = new Node(head.val);
            curr = curr.next;
            randmap.put(head, curr);
            head = head.next;
        }
        Node temp = ans;
        for(Node key : randmap.keySet()){
            Node copyNode = randmap.get(key);
            copyNode.random = randmap.get(key.random);
        }
        return ans;
    }
}
