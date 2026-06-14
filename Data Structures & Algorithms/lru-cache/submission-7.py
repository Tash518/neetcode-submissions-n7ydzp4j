class Node:
    def __init__(self, key=0, val=0, next=None, prev=None) -> None: 
        self.key = key 
        self.val = val 
        self.next = next 
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.size = 0 
        self.hashmap = {} 
        #usin dummy
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def removeNode(self, cur):
        prev, nxt = cur.prev, cur.next
        prev.next = nxt
        nxt.prev = prev

    def insertNode(self, node):
        #insert riht after dummy head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def moveToHead(self,node):
        #remove then move to front
        self.removeNode(node)
        self.insertNode(node)

    
        

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        cur = self.hashmap[key]
        self.moveToHead(cur)
        return cur.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            cur = self.hashmap[key]
            cur.val = value
            self.moveToHead(cur)
        else:
            newnode = Node(key=key, val=value)
            self.hashmap[key] = newnode
            self.insertNode(newnode)
            self.size+=1

            if self.size>self.capacity:
                lru = self.tail.prev
                self.removeNode(lru)
                del self.hashmap[lru.key]
                self.size-=1
        



            
        
