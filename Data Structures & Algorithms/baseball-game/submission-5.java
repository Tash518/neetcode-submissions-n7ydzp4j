class Solution {
    public int calPoints(String[] operations) {
       Stack<Integer> record = new Stack<>();
       for(String c : operations){
        if(c.equals("+")){
            int a=record.pop();
            int b=record.peek();
            record.push(a);
            record.push(a+b);
        }
        else if(c.equals("D")){
            record.push(2*record.peek());
        }
        else if(c.equals("C")){
            record.pop();
        }
        else{
            record.add(Integer.parseInt(c));
        }
       }
       int sum=0;
       for(int i : record){
            sum+=i;
       }
       return sum;
    }
}