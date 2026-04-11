class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        for(int x:asteroids){
            boolean dest = false;
            while(!stack.isEmpty() && stack.peek()>0 && x<0){
                if(stack.peek()<-x){
                    stack.pop();
                    continue;
                }
                else if (stack.peek()==-x){
                    stack.pop();
                    dest = true;
                    break;
                }else{
                    dest=true;
                    break;
                }
            }
            if(!dest){
                stack.push(x);
            }
        }
        int[] result = new int[stack.size()];
        for(int i=stack.size()-1;i>=0;i--){
            result[i]=stack.pop();
        }
        return result;
    }
}