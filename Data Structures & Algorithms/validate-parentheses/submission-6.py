class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for x in s:
            if x=='(' or x=='[' or x=='{':
                stack.append(x)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if x==')' and top!='(' or x==']' and top!='[' or x=='}' and top!='{':
                    return False
        return not stack