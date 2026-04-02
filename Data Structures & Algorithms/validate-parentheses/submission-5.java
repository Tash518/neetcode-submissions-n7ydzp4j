
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character,Character> checkmap = new HashMap<>();
        checkmap.put('}', '{');
        checkmap.put(')', '(');
        checkmap.put(']', '[');
        for(char x :s.toCharArray()){
            if( checkmap.containsKey(x)){
                if(stack.isEmpty() || stack.peek()!=checkmap.get(x)){
                    return false;
                }
                stack.pop();
            }else{
                stack.push(x);
            }
        }
        return stack.isEmpty();

    }
}
