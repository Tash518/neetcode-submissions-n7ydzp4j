class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int rows = obstacleGrid.length;
        int cols = obstacleGrid[0].length;

        int[][] dp = new int[rows][cols];

        if (obstacleGrid[rows - 1][cols - 1] == 1 || obstacleGrid[0][0] == 1)
            return 0;
        dp[rows - 1][cols - 1] = 1;

        // last col
        for (int i = rows - 2; i > -1; i--) {
            if (obstacleGrid[i][cols - 1] == 1)
                dp[i][cols - 1] = 0;
            else
                dp[i][cols - 1] = dp[i + 1][cols - 1];
        }
        // last row
        for (int i = cols - 2; i > -1; i--) {
            if (obstacleGrid[rows - 1][i] == 1)
                dp[rows - 1][i] = 0;
            else
                dp[rows - 1][i] = dp[rows - 1][i + 1];
        }

        for (int row = rows - 2; row > -1; row--) {
            for (int col = cols - 2; col > -1; col--) {
                if (obstacleGrid[row][col] == 1)
                    dp[row][col] = 0;
                else
                    dp[row][col] = dp[row][col + 1] + dp[row + 1][col];
            }
        }

        return dp[0][0];
    }
}