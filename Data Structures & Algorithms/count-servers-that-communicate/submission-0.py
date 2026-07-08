class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rowcount = [0]*m
        colcount = [0]*n

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    rowcount[i]+=1
                    colcount[j]+=1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (rowcount[i]>1 or colcount[j]>1):
                    ans+=1
        return ans