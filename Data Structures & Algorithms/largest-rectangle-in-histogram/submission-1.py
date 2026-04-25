class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        maxarea=0
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                top=stack.pop()
                height=heights[top]
                if not stack:
                    width=i
                else:
                    width=i-stack[-1]-1
                maxarea=max(maxarea,height*width)
            stack.append(i)
        while stack:
            top=stack.pop()
            height=heights[top]
            if not stack:
                width=n
            else:
                width=n-stack[-1]-1
            maxarea=max(maxarea,height*width)
        return maxarea
            