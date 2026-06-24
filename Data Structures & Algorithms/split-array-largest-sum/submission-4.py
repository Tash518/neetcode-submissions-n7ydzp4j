class Solution:

    def splitArray(self, nums: List[int], k: int) -> int:
        MAX = float('inf')
        n = len(nums)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        dp = [[MAX]*(k+1) for _ in range(n+1)]

        #base
        for i in range(n+1):
            dp[i][1] = prefix[i]
        for K in range(2,k+1):
            for i in range(1,n+1):
                for j in range(K-1,i):
                    dp[i][K] = min(dp[i][K],max(dp[j][K-1], prefix[i]-prefix[j]))
        return dp[n][k]
