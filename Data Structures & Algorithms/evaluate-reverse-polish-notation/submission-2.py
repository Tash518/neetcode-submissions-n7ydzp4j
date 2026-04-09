class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for x in tokens:

            if x=="+":
                a= stack.pop()
                b=stack.pop()
                stack.append(a+b)
                print("add ", stack)
            elif x=="*":
                a= stack.pop()
                b=stack.pop()
                stack.append(a*b)
                print("mul ", stack)
            elif x=="/":
                a= stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
                print("div ", stack)
            elif x=="-":
                a= stack.pop()
                b=stack.pop()
                stack.append(b-a)
                print("sub ", stack)
            else:
                stack.append(int(x))
                print("num push ", stack)
        return stack[-1]
            