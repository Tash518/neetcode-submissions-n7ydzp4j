class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top,bottom = 0,len(matrix)-1
        left,right=0,len(matrix[0])-1
        ans = [0] * ((bottom+1) * (right+1))
        idx=0
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                ans[idx]=matrix[top][i]
                idx+=1
            top+=1
            for i in range(top,bottom+1):
                ans[idx]=matrix[i][right]
                idx+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans[idx]=matrix[bottom][i]
                    idx+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans[idx]=matrix[i][left]
                    idx+=1
                left+=1
        return ans
