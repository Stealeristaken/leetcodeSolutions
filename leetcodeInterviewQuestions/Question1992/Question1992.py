from typing import List
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        R, C = len(land), len(land[0])
        res = []

        def dfs(r, c):
            nonlocal mn, mx
            if r >= 0 and r < R and c >= 0 and c < C and land[r][c] == 1:
                land[r][c] = 0
                mn = (min(mn[0], r), min(mn[1], c))
                mx = (max(mx[0], r), max(mx[1], c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        for r in range(R):
            for c in range(C):
                if land[r][c] == 1:
                    mn, mx = (R, C), (0, 0)
                    dfs(r, c)
                    res.append([*mn,*mx])
        return res
  
################ 

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n, res = len(land), len(land[0]), []
        for i in range(m):
            j = 0
            while j < n:
                if land[i][j]:
                    if land[i][j] == 1:
                        k, l = j+1, i+1
                        while k < n and land[i][k]==1: k += 1
                        k += 1
                        while l < m and land[l][j]==1:
                            land[l][j] = -k
                            l += 1
                        if l < m:
                            land[l][j] = 1-k
                        res.append([i,j,l-1,k-2])
                        j = k
                    else:
                        j = -land[i][j]
                else:
                    j += 1
        return res