class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int rows = triangle.size();
        int cols = triangle.get(rows-1).size();

        Integer[][] dp = new Integer[rows][cols];

        solve(dp, triangle,0,0);
        return dp[0][0];

    }
    private int solve(Integer[][] dp, List<List<Integer>> triangle, int row, int col){
        if(row == triangle.size()-1){
            dp[row][col] = triangle.get(row).get(col);
            return dp[row][col];
        }
        if(dp[row][col] != null){
            return dp[row][col];
        }
        int min = Math.min(solve(dp,triangle, row+1,col), solve(dp,triangle, row+1,col+1));
        dp[row][col] = min+triangle.get(row).get(col);
        return dp[row][col];
    }
}