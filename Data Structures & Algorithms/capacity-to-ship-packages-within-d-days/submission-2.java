class Solution {
    private int numdays(int[] weights, int maxw){
        int days=1;
        int curw=0;
        for(int w : weights){
            if(w+curw <=maxw){
                curw+=w;
            }else{
                days++;
                curw=w;
            }
        }
        return days;
    }
    public int shipWithinDays(int[] weights, int days) {
        int low = 0;
        int high=0;
        for(int w : weights){
            low = Math.max(low,w);
            high+=w;
        }
        int ans = high;
        while(low<=high){
            int mid = (low+high)/2;
            System.out.println(mid);
            int time = numdays(weights, mid);
            if( time<=days){
                ans=mid;
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }
        return ans;
    }
}