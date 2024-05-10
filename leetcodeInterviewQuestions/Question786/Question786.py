import heapq
from typing import List
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        heap = []
        heapq.heapify(heap)

        for p in arr:
            for q in arr:
                if q < p:
                    continue

                heapq.heappush(heap, (p/q, (p, q)))

        for _ in range(k - 1):
            heapq.heappop(heap)

        return list(heapq.heappop(heap)[1])