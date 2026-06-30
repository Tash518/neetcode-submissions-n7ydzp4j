class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        ArrayList<Integer> tails = new ArrayList<>();

        for (int num : nums) {
            int left = 0;
            int tail_length = tails.size();
            int right = tail_length - 1;

            while (left <= right) {
                int mid = left + (right - left) / 2;

                if (tails.get(mid) < num) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            if (left == tail_length) {
                tails.add(num);
            } else {
                tails.set(left, num);
            }
        }
        return tails.size();
    }
}