class Solution {
    public String minWindow(String s, String t) {
        if(s.length()==0 ||t.length()==0){
            return "";
        }
        HashMap<Character, Integer> t_freq = new HashMap<>();
        for(char c : t.toCharArray()){
            t_freq.put(c,t_freq.getOrDefault(c, 0)+1);
        }
        int required = t_freq.size();
        int formed = 0,left=0;

        HashMap<Character, Integer> w_freq = new HashMap<>();
        int minlen = Integer.MAX_VALUE;
        int finalleft=0,finalright=0;

        for(int right=0;right<s.length();right++){
            char ch = s.charAt(right);
            w_freq.put(ch,w_freq.getOrDefault(ch, 0)+1);
            if(t_freq.containsKey(ch) && w_freq.get(ch)==t_freq.get(ch)){
                formed++;
            }
            while(formed==required){
                if(right-left+1<minlen){
                    minlen=right-left+1;
                    finalleft=left;
                    finalright=right;
                }
                char lch = s.charAt(left);
                w_freq.put(lch, w_freq.get(lch)-1);
                if(t_freq.containsKey(lch) && w_freq.get(lch)<t_freq.get(lch)){
                    formed-=1;
                }
                if(w_freq.get(lch)==0){
                    w_freq.remove(lch);
                }
                left++;
            }
        }
        return (minlen==Integer.MAX_VALUE) ? "" : s.substring(finalleft, finalright+1);
        
    }
}
