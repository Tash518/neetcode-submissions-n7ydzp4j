class FreqStack:

    def __init__(self):
        self.freq=defaultdict()
        self.groups=defaultdict(list)
        self.maxfreq=0

    def push(self, val: int) -> None:
        f = self.freq.get(val,0)+1
        self.freq[val]=f
        if f>self.maxfreq:
            self.maxfreq=f
        self.groups[f].append(val)
    def pop(self) -> int:
        val = self.groups[self.maxfreq].pop()
        self.freq[val]-=1
        if not self.groups[self.maxfreq]:
            self.maxfreq-=1
        return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()