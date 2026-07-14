class Solution {

    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] < b[0])
                return -1;
            if (a[0] > b[0])
                return 1;
            return 0;
        });
        ArrayList<int[]> merged = new ArrayList<>();
        for (int[] interval : intervals) {
            int start = interval[0];
            int end = interval[1];
            int mergedsize = merged.size();
            if (mergedsize == 0 || merged.get(mergedsize - 1)[1] < start) {
                merged.add(interval);
            } else {
                int[] last = merged.get(mergedsize - 1);
                last[1] = Math.max(last[1], end);
            }
        }
        return merged.toArray(new int[merged.size()][]);
    }
}