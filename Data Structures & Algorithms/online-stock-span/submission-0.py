class StockSpanner:

    def __init__(self):
        self.prices=[]

    def next(self, price: int) -> int:
        if not self.prices:
            self.prices.append(price)
            return 1
        self.prices.append(price)
        return self.getprevsgreater(self.prices)
        

        
    def getprevsgreater(self, arr):
        stack=[]
        result=[]
        for i in range(len(arr)):
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
            if not stack:
                result.append(i+1)
            else:
                result.append( i-stack[-1])
            stack.append(i)
        return result[-1]



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)