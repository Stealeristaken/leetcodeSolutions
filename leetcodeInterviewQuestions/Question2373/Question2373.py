from typing import List
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        res = [([0] * (n - 2)) for _ in range(n - 2)]

        for x in range(n - 2):
            for y in range(n - 2):
                local_max = 0
                for i in range(x, x + 3):
                    for j in range(y, y + 3):
                        local_max = max(local_max, grid[i][j])
                res[x][y] = local_max

        return res
  
  
  
  
################################## 


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)
        res =[]
        for i in range(length-2):
            temp=[]
            for j in range(length-2):
                maxi = max(grid[i][j],grid[i][j+1],grid[i][j+2],
                           grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],
                           grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2])
                temp.append(maxi)
            res.append(temp)
        return res