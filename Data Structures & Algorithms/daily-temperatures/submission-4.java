class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        ArrayDeque<Integer>stack = new ArrayDeque<>();
        int[] result = new int[n];
        for(int i=n-1;i>-1;i--){
            while(!stack.isEmpty() && temperatures[stack.peek()]<=temperatures[i]){
                stack.pop();
            }
            if(!stack.isEmpty()){
                result[i]=stack.peek()-i;
            }
            stack.push(i);
        }
        return result;
    }
}
