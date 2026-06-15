class Node {
    public int key;
    public int val;
    public Node next;
    public Node prev;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
        this.next = null;
        this.prev = null;
    }
    public Node() {
        this.next = null;
        this.prev = null;
    }
}

class LRUCache {
    int capacity, size;
    Node head, tail;
    HashMap<Integer, Node> hashmap;
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        hashmap = new HashMap<>();
        head = new Node();
        tail = new Node();
        head.next = tail;
        tail.prev = head;
    }

    void removeNode(Node cur) {
        Node prev = cur.prev;
        Node next = cur.next;
        prev.next = next;
        next.prev = prev;
    }

    void insertNode(Node node) {
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }

    void moveToHead(Node node) {
        removeNode(node);
        insertNode(node);
    }

    public int get(int key) {
        if (!hashmap.containsKey(key))
            return -1;

        Node cur = hashmap.get(key);
        moveToHead(cur);
        return cur.val;
    }

    public void put(int key, int value) {
        if (hashmap.containsKey(key)) {
            Node cur = hashmap.get(key);
            cur.val = value;
            moveToHead(cur);
        } else {
            Node newnode = new Node(key, value);
            hashmap.put(key, newnode);
            insertNode(newnode);
            size++;
        }
        if (size > capacity) {
            Node lru = tail.prev;
            removeNode(lru);
            hashmap.remove(lru.key);
            size--;
        }
    }
}
