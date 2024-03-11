class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n=len(mat)
        m=len(mat[0])
        rows=[]
        columns=[]
        x=0
        for i in range(n):
            if x in  (mat[i]):
                rows.append(i)
            for j in range(m):
                if mat[i][j]==0:
                    columns.append(j)

        for i in rows:
            for j in range(m):
                mat[i][j]=0

        for j in columns:
            for i in range(n):
                mat[i][j]=0
