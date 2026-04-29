class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        colset = set()
        rowset = set()
        c,r = len(matrix),len(matrix[0])
        for i in range(c):
            for j in range(r):
                if matrix[i][j]==0:
                    colset.add(i)
                    rowset.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in colset or j in rowset:
                    matrix[i][j]=0
        