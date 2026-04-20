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
            elif s[i]=="[":
                print("curstr, ",curstr)
                numstack.append(k)
                strstack.append(curstr)
                k=0
                curstr=[]
            elif s[i]=="]":
                count=numstack.pop()
                prev = strstack.pop()
                cur = count*curstr
                curstr = prev+cur
            else:
                curstr.append(s[i])
            i+=1
        return ("".join(curstr))