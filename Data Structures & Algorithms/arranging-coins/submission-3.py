class Solution:
    def arrangeCoins(self, n: int) -> int:
    
        if n<2:
            return n
        low,high = 0, n//2
        ans = 0
        while low<=high:
            mid = (low+high)//2
            coins = mid*(mid+1)//2
            if coins==n:
                return mid
            if coins<n:
                ans=mid
                low = mid+1
            else:
                high = mid-1
        return ans
    