class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        ArrayDeque<Integer>stack = new ArrayDeque<>();
        int[] result = new int[n];
        for(int i=0;i<n;i++){
            int curr = temperatures[i];
            while(!stack.isEmpty() && curr>temperatures[stack.peek()]){
                int previous=stack.pop();
                result[previous] = i-previous;
            }
            stack.push(i);
        }
        return result;
    }
}
