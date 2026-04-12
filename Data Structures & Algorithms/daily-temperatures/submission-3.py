class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        result=[0]*n
        for i in range(n):
            curr=temperatures[i]
            while stack and curr>temperatures[stack[-1]]:
                previous=stack.pop()
                result[previous]=i-previous
            stack.append(i)

        return result