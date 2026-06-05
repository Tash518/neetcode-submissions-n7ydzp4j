class Node:
        def __init__(self, val=0, next = None):
            self.val = val
            self.next = next
class MyCircularQueue:
    

    def __init__(self, k: int):
        self.maxSize = k
        self.size = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        newnode = Node(value)
        if self.isEmpty():
            self.head = self.tail = newnode
            self.tail.next = self.head
        else:
            newnode.next = self.head
            self.tail.next = newnode
            self.tail = newnode
        self.size+=1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.size==1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size-=1
        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val
    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==self.maxSize


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()