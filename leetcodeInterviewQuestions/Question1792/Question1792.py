import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], k: int) -> float:
        heap = []

        for x, y in classes:
            currRatio = x / y
            increasedRatio = (x + 1) / (y + 1)

            heapq.heappush(heap, (-(increasedRatio - currRatio), currRatio, (x + 1, y + 1)))
        
        while k > 0:
            diff, ratio, (x, y) = heapq.heappop(heap)
            newRatio = (x + 1) / (y + 1)
            newDiff = newRatio - (-diff + ratio)
            heapq.heappush(heap, (-newDiff, x / y, (x + 1, y + 1)))

            k -= 1
        
        sumi = 0
        for a, b, c in heap:
            sumi += b

        return sumi / len(heap)