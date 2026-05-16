class TimeMap {
    private HashMap<String, ArrayList<Object[]>> timemap;
    public TimeMap() {
        timemap = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        timemap.computeIfAbsent(key, k -> new ArrayList<>()).add(new Object[]{value, timestamp});

    }
    
    public String get(String key, int timestamp) {
        if(!timemap.containsKey(key)) return "";
        ArrayList<Object[]> req = timemap.get(key);
        if((int)req.get(0)[1]>timestamp) return "";
        if((int)req.get(req.size()-1)[1]<=timestamp){
            return (String)req.get(req.size()-1)[0];
        }
        int l=0,r=req.size()-1;
        String ans = "";
        while(l<=r){
            int mid = l +(r-l)/2;
            if((int)req.get(mid)[1]<=timestamp){
                ans = (String)req.get(mid)[0];
                l=mid+1;
            }else{
                r=mid-1;
            }
        }
        return ans;
    }
}
