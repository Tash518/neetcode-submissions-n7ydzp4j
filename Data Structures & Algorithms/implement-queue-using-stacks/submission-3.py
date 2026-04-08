class MyQueue:

    def __init__(self):
        self.stackin=[]
        self.stackout=[]

    def push(self, x: int) -> None:
        self.stackin.append(x)
    def pop(self) -> int:
        if not self.stackout:
            while self.stackin:
                self.stackout.append(self.stackin.pop())
        return self.stackout.pop()

    def peek(self) -> int:
        if not self.stackout:
            while self.stackin:
                self.stackout.append(self.stackin.pop())
        return self.stackout[-1]
        
    def empty(self) -> bool:
        return not self.stackout and not self.stackin
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()