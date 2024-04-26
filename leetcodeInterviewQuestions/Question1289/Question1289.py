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

        