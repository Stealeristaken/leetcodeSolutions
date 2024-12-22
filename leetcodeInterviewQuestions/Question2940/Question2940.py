from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        res = [-1] * len(queries)

        for i, q in enumerate(queries):
            l, r = sorted(q)
            if l == r or heights[l] < heights[r]:
                res[i] = r
            else :
                h = max(heights[l], heights[r])
                groups[r].append((h, i))
        
        minheap = []
        for i, h in enumerate(heights):
            for q_h, q_i in groups[i]:
                heappush(minheap, (q_h, q_i))
            while minheap and h > minheap[0][0]:
                qh, qi = heappop(minheap)
                res[qi] = i
        return res