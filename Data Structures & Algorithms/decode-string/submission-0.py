class Solution:
    def decodeString(self, s: str) -> str:
        strstack=[]
        numstack=[]
        i,n=0,len(s)
        k=0
        curstr = []
        while i<n:
            if s[i].isdigit():
                k=10*k+int(s[i])
                i+=1
            elif s[i]=="[":
                print("curstr, ",curstr)
                numstack.append(k)
                substr = "".join(curstr)
                strstack.append(substr)
                k=0
                curstr=[]
                i+=1
            elif s[i]=="]":
                count=numstack.pop()
                prev = strstack.pop()
                curstr = list(prev+count*"".join(curstr))
                i+=1
            else:
                curstr.append(s[i])
                i+=1
        return ("".join(curstr))