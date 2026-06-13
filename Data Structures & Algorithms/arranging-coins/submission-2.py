class Solution:
    def arrangeCoins(self, n: int) -> int:
        def solve(x):
            if x<2:
                return x
            low,high = 0, x//2
            ans = 0
            while low<=high:
                mid = (low+high)//2
                coins = mid*(mid+1)//2
                if coins==x:
                    return mid
                if coins<x:
                    ans=mid
                    low = mid+1
                else:
                    high = mid-1
            return ans
        return solve(n)