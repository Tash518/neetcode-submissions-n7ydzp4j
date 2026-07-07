class Solution {
    void dfs(int[][] image, int rows, int cols, int origcol, int color ,int r, int c){
        if(r<0 || r>=rows || c<0 || c>=cols ||image[r][c]!=origcol) return;

        image[r][c] = color;
        dfs(image, rows,cols,origcol,color,r+1,c);
        dfs(image, rows,cols,origcol,color,r-1,c);
        dfs(image, rows,cols,origcol,color,r,c+1);
        dfs(image, rows,cols,origcol,color,r,c-1);

    }
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int origcol = image[sr][sc];
        int rows = image.length;
        int cols = image[0].length;

        if( origcol==color) return image;

        dfs(image, rows,cols,origcol,color,sr,sc);
        return image;
    }
}