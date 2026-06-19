/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */

class Solution {
    private int searchMountain(MountainArray m, int t,int low,int high,boolean asc){
        while(low<=high){
            int mid = low+(high-low)/2;
            int val = m.get(mid);

            if(val==t) return mid;

            if(asc){
                if( val<t) low = mid+1;
                else high = mid-1;
            }else{
                if( val<t) high = mid-1;
                else low = mid+1;
            }
        }
        return -1;
    }
    
    public int findInMountainArray(int target, MountainArray mountainArr) {
        int size = mountainArr.length();
        int low=0,high=size-1;

        while(low<high){
            int mid = low+(high-low)/2;

            int val = mountainArr.get(mid);
            if( val< mountainArr.get(mid+1)){
                low = mid+1;
            }
            else{
                high = mid-1;
            }
        }

        int peak = low;
        int l = searchMountain(mountainArr, target, 0, peak, true);
        if(l!=-1) return l;
        return searchMountain(mountainArr, target, peak+1, size-1, false);


    }
}