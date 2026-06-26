class Solution:

    def splitArray(self, nums: List[int], k: int) -> int:
        def checksplit(max_sum):
            count = 1
            cursum = 0
            for num in nums:
                if cursum+num>max_sum:
                    cursum = num
                    count+=1
                else:
                    cursum+=num
            return count<=k

        left = max(nums)
        right = sum(nums)
        while left<right:
            mid = (left+right)//2

            if checksplit(mid):
                right = mid
            else:
                left = mid+1
        return left