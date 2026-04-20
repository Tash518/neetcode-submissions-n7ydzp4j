class Solution {
    public String decodeString(String s) {
        Stack<StringBuilder> strstack = new Stack<>();
        Stack<Integer> numstack = new Stack<>();
        StringBuilder curstr = new StringBuilder();
        int k=0;
        for(char ch : s.toCharArray()){
            if(Character.isDigit(ch)){
                k=10*k+(ch-'0');
            }
            else if(ch=='['){
                numstack.push(k);
                strstack.push(curstr);
                curstr = new StringBuilder();
                k=0;
            }
            else if(ch==']'){
                StringBuilder prev = strstack.pop();
                int count = numstack.pop();
                for(int i=0;i<count;i++){
                    prev.append(curstr);
                }
                curstr=prev;
            }
            else{
                curstr.append(ch);
            }
        }
        return curstr.toString();
    }
}