class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [row[:] for row in triangle]
        for row in range(n-2,-1,-1):
            for col in range(len(triangle[row])):
                dp[row][col] += min(dp[row+1][col], dp[row+1][col+1])

            
        return dp[0][0]