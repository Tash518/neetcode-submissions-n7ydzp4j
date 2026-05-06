class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int low = 1;
        int high = 0;
        for (int x : piles) {
            high = Math.max(x, high);
        }
        int ans = 0;
        int times = 0;
        while (low <= high) {
            int time = 0;
            int mid = low+(high - low) / 2;
            for (int pile : piles) {
                time += (pile+mid-1)/mid;
            }
            if (time <= h) {
                high = mid - 1;
                ans = mid;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
}
