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
        self.head = self.tail = None
        
    
    
        

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        cur = self.hashmap[key]
        val = cur.val
        if not cur.prev :#is head
            return val
        if not cur.next:#is tail
            self.tail = cur.prev
            self.tail.next = None
            cur.prev = None
            cur.next = self.head
            self.head.prev = cur
            self.head = cur
        #node in mid move to head
        else:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            cur.prev = None
            cur.next = self.head
            self.head.prev = cur
            self.head = cur
        return val
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            cur = self.hashmap[key]
            cur.val = value
            if cur==self.head:
                return
            #cut cur from neighbour
            if cur.prev:
                cur.prev.next = cur.next
            if cur.next:
                cur.next.prev = cur.prev
            #set tail
            if cur == self.tail:
                self.tail = cur.prev
                self.tail.next = None
            self.head.prev = cur
            cur.next = self.head
            cur.prev = None
            self.head = cur
        else:
            newnode = Node(key=key, val=value)
            self.hashmap[key] = newnode
            if not self.head:
                self.head = self.tail = newnode
                self.size+=1
                return
            if self.size<self.capacity:
                self.head.prev = newnode
                newnode.next = self.head
                self.head = newnode
                self.size +=1
            else:
                oldtail = self.tail
                del self.hashmap[oldtail.key]

                if oldtail.prev:
                    self.tail = oldtail.prev
                    self.tail.next = None
                else:
                    self.head = self.tail = None
                if not self.head:
                    self.head = self.tail = newnode
                    self.size+=1
                else:
                    self.head.prev = newnode
                    newnode.next = self.head
                    self.head = newnode
        return



            
        
