class Solution {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<>();
        String[] parts = path.split("/");
        for(String part : parts){
            if(part.equals("..")){
                if(!stack.isEmpty()){
                    stack.pop();
                }
            }
            else if(!part.equals("") && !part.equals(".")){
                stack.push(part);
            }
        }
        StringBuilder result = new StringBuilder();
        for(String part: stack){
            result.append("/").append(part);
        }
        return result.length()==0?"/":result.toString();

    }
}