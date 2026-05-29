class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length;
        int total=0;
        for(int x : cardPoints){
            total+=x;
        }
        if(k==n) return total;
        int winSize = n-k;
        int winSum=0;
        for(int i=0;i<winSize;i++){
            winSum+=cardPoints[i];
        }
        int minSum = winSum;
        for(int i= winSize;i<n;i++){
            winSum += cardPoints[i]-cardPoints[i-winSize];
            minSum = Math.min(winSum,minSum);
        }
        return total-minSum;
    }
}