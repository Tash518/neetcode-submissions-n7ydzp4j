class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int t = 0, b = rows - 1;
        int r1 = 0;
        while (t <= b) {
            int mid = (t + b) / 2;
            if (matrix[mid][0] == target) {
                return true;
            } else if (matrix[mid][0] < target) {
                r1 = mid;
                t = mid + 1;
            } else {
                b = mid - 1;
            }
        }
        int l = 0, r = cols - 1;
        while (l <= r) {
            int mid = (r + l) / 2;
            if (matrix[r1][mid] == target) {
                return true;
            } else if (matrix[r1][mid] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return false;
    }
}
