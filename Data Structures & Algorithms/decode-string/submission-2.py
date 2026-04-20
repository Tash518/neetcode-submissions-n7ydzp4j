class Solution:
    def decodeString(self, s: str) -> str:
        strstack=[]
        numstack=[]
        k,curstr=0,[]
        for ch in s:
            if ch.isdigit():
                k=10*k+int(ch)
            elif ch=="[":
                numstack.append(k)
                strstack.append(curstr)
                curstr,k=[],0
                
            elif ch=="]":
                prev = strstack.pop()
                prev.extend(numstack.pop()*curstr)
                curstr=prev
            else:
                curstr.append(ch)
        return ("".join(curstr))