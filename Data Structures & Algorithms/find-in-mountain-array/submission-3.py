class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        cache = {}

        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]
        size = mountainArr.length()
        low, high = 0, size-1
        while low<high:
            mid = (low+high)//2

            val = get(mid)
            if val<get(mid+1):
                low = mid+1
            else:
                high = mid
        if get(low)==target: return low
        peak = low
        
        def searchmountain(mountainArr, target, low, peak, asc=True):
            while low<=peak:
                mid = (low+peak)//2
                val = get(mid)
                if val==target: return mid

                if asc:
                    if val<target: 
                        low = mid+1
                    else:
                        peak = mid-1
                    
                else:
                    if val<target: 
                        peak = mid-1
                    else:
                        low = mid+1
                    
            return -1
        l =  (searchmountain(mountainArr, target, 0, peak, asc=True))
        if l!=-1: return l
        return (searchmountain(mountainArr, target, peak+1, size-1, asc=False))





