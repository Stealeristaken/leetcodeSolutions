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