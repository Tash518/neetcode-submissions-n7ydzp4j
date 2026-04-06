class Solution {
    public int calPoints(String[] operations) {
       ArrayList<Integer> record = new ArrayList<>();
       for(String c : operations){
        int size = record.size();
        if(c.equals("+")){
            record.add(record.get(size-1)+record.get(size-2));
        }
        else if(c.equals("D")){
            record.add(2*record.get(size-1));
        }
        else if(c.equals("C")){
            record.remove(size-1);
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