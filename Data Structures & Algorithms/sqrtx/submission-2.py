class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2: return x
        l,r=0,x//2
        ans=0
        while l<=r:
            mid = (l+r)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                l=mid+1
                ans=mid
            else:
                r=mid-1
        return ans