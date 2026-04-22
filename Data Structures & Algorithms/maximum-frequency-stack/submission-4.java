class FreqStack {
    private HashMap<Integer, Integer> freq;
    private HashMap<Integer, Stack<Integer>> groups;
    private int maxfreq;
    public FreqStack() {
        freq = new HashMap<>();
        groups = new HashMap<>();
        maxfreq = 0;
    }
    
    public void push(int val) {
        int f = freq.getOrDefault(val, 0)+1;
        freq.put(val, f);
        maxfreq= f>maxfreq?f:maxfreq;
        if(!groups.containsKey(f)){
            groups.put(f, new Stack<>());
        }
        groups.get(f).push(val);
    }
    
    public int pop() {
        int val = groups.get(maxfreq).pop();
        freq.put(val, freq.get(val)-1);
        if(groups.get(maxfreq).isEmpty()){
            maxfreq--;
        }
        return val;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(val);
 * int param_2 = obj.pop();
 */