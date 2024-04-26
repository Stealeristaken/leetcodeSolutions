from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)==1:
            return grid[0][0]
        dict={}
        
        def dfs(row,col):
            if (row,col) in dict:
                return dict[(row,col)]
            if row>=len(grid):
                return 0
            
            res=float("inf")
            for i in range(len(grid[0])):
                if i!=col :
                    res=min(res,dfs(row+1,i))

            ans=res+grid[row][col]
            dict[(row,col)]=ans
            return ans
        res=float("inf")
        for i in range(len(grid[0])):
            res=min(res,dfs(0,i))
        return res

############# 



class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        DP = grid[0]

        for i in range(1, N):
            indx1 = DP.index(min(DP))
            indx2 = DP.index(min(DP[:indx1] + DP[indx1+1:]))
            for j in range(N):
                if j != indx1:
                    grid[i][j] += DP[indx1]
                else:
                    grid[i][j] += DP[indx2]
            DP = grid[i]

        return min(DP)