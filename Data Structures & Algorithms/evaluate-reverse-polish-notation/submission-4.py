class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for x in tokens:
            if x not in {"+","-","/","*"}:
                stack.append(int(x))
            else:
                if x=="+":
                    a= stack.pop()
                    b=stack.pop()
                    stack.append(a+b)
                elif x=="*":
                    a= stack.pop()
                    b=stack.pop()
                    stack.append(a*b)
                elif x=="/":
                    a= stack.pop()
                    b=stack.pop()
                    stack.append(int(b/a))
                elif x=="-":
                    a= stack.pop()
                    b=stack.pop()
                    stack.append(b-a)
            
        return stack[0]
            