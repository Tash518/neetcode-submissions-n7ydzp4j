class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack1=[]
        pse=[-1]*n
        for i in range(n):
            while stack1 and heights[stack1[-1]]>=heights[i]:
                stack1.pop()
            if stack1:
                pse[i]=stack1[-1]
            stack1.append(i)
        stack2=[]
        nse=[n]*n
        for i in range(n-1,-1,-1):
            while stack2 and heights[stack2[-1]]>=heights[i]:
                stack2.pop()
            if stack2:
                nse[i]=stack2[-1]
            stack2.append(i)

        maxarea=0
        for i in range(n):
            cur = heights[i]*(nse[i]-pse[i]-1)
            maxarea=max(maxarea,cur)
        return maxarea

        