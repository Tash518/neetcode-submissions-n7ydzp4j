class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for x in s:
            if x in {'{','(','['}:
                stack.append(x)
            else:
                if not stack:
                    return False
                else:
                    if x==']' and stack[-1]!='[':
                        return False
                    elif x==']' and stack[-1]=='[':
                        stack.pop()
                    if x==')' and stack[-1]!='(':
                        return False
                    elif x==')' and stack[-1]=='(':
                        stack.pop()
                    if x=='}' and stack[-1]!='{':
                        return False
                    elif x=='}' and stack[-1]=='{':
                        stack.pop()
        
        return True if not stack else False