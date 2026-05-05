class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def numdays(weights,maxw):
            days,curw=1,0
            for i in weights:
                if i+curw<=maxw:
                    curw+=i
                else:
                    days+=1
                    curw=i
            return days

        ans = low = max(weights)
        high = total = sum(weights)
        print("high,low ",total,low)
        
        while low <= high:
            mid  = (low+high)//2
            time  = numdays(weights, mid)
            print("current max = ", mid,", time  = ", time)
            if time<=days:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
        