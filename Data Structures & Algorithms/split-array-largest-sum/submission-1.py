from functools import lru_cache
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        @lru_cache(None)
        def solve(k, index):
            if k==1:
                return sum(nums[index:])

            best = float('inf')
            currentSum = 0
            for i in range(index,len(nums)+1-k):
                currentSum+=nums[i]
                nextSum = solve(k-1,i+1)
                best = min(best,max(currentSum, nextSum))
            return best

        return(solve(k,0))
