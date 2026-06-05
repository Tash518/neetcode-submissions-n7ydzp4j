class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        cols = len(triangle[rows-1])
        
        dp =[[float('-inf')]*cols for _ in range(rows)]
        def solve(dp, triangle, row, col):
            if row == len(triangle)-1:
                dp[row][col] = triangle[row][col]
                return triangle[row][col]
            if dp[row][col]!=float('-inf'): return dp[row][col]
            min_ = min(solve(dp, triangle, row+1, col), solve(dp, triangle, row+1, col+1))

            dp[row][col] = min_+triangle[row][col]
            return dp[row][col]
        solve(dp, triangle, 0,0)
        return dp[0][0]
            
