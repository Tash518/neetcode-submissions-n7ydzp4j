class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for(String x : tokens){
            if( x.equals("+")){
                int a= stack.pop();
                int b=stack.pop();
                stack.push(a+b);
                }
            else if(x.equals("*")){
                int a= stack.pop();
                int b=stack.pop();
                stack.push(a*b);
                }
            else if(x.equals("/")){
                int a= stack.pop();
                int b=stack.pop();
                stack.push(b/a);
                }
            else if(x.equals("-")){
                int a= stack.pop();
                int b=stack.pop();
                stack.push(b-a);}
            else{
                stack.push(Integer.parseInt(x));}
        }
        return stack.peek();
    }
}
