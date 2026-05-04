class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo,hi = 1,max(piles)
        ans=time=0
        while lo<=hi:
            time=0
            mid = (lo+hi)//2
            for pile in piles:
                time += math.ceil(pile/mid)
            if time <=h:
                hi = mid-1
                ans=mid

            else:
                lo = mid+1
        return (ans)
