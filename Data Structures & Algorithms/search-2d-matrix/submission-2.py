class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        t,b = 0,rows-1
        r1=0
        while t<=b:
            mid=(t+b)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<target:
                r1=mid
                t=mid+ 1
            else:
                b=mid-1
        l,r=0,cols-1
        while l<=r:
            mid = (l+r)//2
            if matrix[r1][mid]==target:
                return True
            elif matrix[r1][mid]<target:
                l=mid+ 1
            else:
                r=mid-1
        return False