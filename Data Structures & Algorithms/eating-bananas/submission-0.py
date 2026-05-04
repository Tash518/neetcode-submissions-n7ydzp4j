class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = max(piles)
        lo = 1
        ans=time=0
        
        while lo<=hi:
            mid = (lo+hi)//2
            print("mid = ", mid)
            for pile in piles:
                time += math.ceil(pile/mid)
            print("cur time- ", time)
            if time <=h:
                hi = mid-1
                ans=mid
                time=0

            else:
                lo = mid+1
                time=0
        return (ans)
