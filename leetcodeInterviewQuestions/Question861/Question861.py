from typing import List 
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
            n = len(grid)
            m = len(grid[0])
            for i in range(n):
                  if grid[i][0] == 0:
                        for j in range(m):
                              grid[i][j] = 1 - grid[i][j]
            for j in range(1, m):
                  count = 0
                  for i in range(n):
                        count += grid[i][j]
                  if count < n - count:
                        for i in range(n):
                              grid[i][j] = 1 - grid[i][j]
            res = 0
            for i in range(n):
                  for j in range(m):
                        res += grid[i][j] * (1 << (m - 1 - j))
            return res