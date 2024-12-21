from collections import defaultdict
from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        res = 0
        adj = defaultdict(list)
        for s,e in edges:
            adj[s].append(e)
            adj[e].append(s)

        def dfs(cur, par):
            nonlocal res
            total = values[cur]

            for child in adj[cur]:
                if child != par:
                    total += dfs(child, cur)
            if total % k == 0 :
                res += 1
            return total

        dfs(0, -1)
        return res
        