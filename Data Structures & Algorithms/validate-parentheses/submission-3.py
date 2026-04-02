class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        checkmap = {'}':'{',')':'(',']':'['}
        for x in s:
            if x in checkmap:
                if not stack or stack[-1]!=checkmap[x]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(x)
        return not stack