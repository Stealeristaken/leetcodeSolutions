import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        result = float("inf")
        ratio = []
        n = len(quality)
        for i in range(n):
            ratio.append((wage[i]/quality[i],quality[i]))
        ratio.sort(key=lambda p:p[0])
        maxHeap = []
        total_quality = 0
        for rate,q in ratio:
            heapq.heappush(maxHeap,-q)
            total_quality += q
            if len(maxHeap) > k:
                total_quality += heapq.heappop(maxHeap)
            if len(maxHeap) == k:
                result = min(result,total_quality*rate)
        return result