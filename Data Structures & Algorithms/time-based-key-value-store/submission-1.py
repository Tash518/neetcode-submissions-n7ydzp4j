class TimeMap:

    def __init__(self):
        self.timemap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key]=[]
        self.timemap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        req = self.timemap.get(key,[])
        l,r = 0,len(req)-1
        ans=""
        while l<=r:
            mid = (l+r)//2
            if req[mid][1]<=timestamp:
                ans = req[mid][0];
                l=mid+1
            else:
                r=mid-1
        return "" if not ans else ans