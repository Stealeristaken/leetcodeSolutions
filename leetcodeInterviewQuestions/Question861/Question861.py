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
      
############################################################################################################      
      
from collections import defaultdict      
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        rows,cols = len(grid),len(grid[0])
        for r in range(rows):
            if grid[r][0] == 0:
                for c in range(cols):
                    if grid[r][c] == 0:
                        grid[r][c] = 1
                    else:
                        grid[r][c] = 0

        counts = defaultdict(int)
        for c in range(1,cols):
            for r in range(rows):
                if grid[r][c] == 0:
                    counts[c] += 1

        res = rows * (2**(cols-1))
        for c in range(1,cols):
            res += max(counts[c],rows - counts[c])*2**(cols - c - 1)

        return res

            