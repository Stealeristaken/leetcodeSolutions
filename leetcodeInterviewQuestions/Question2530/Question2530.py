import heapq
import math
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap, -1*i)
        score = 0
        for i in range(k):
            val = -1 * heapq.heappop(heap)
            score += val
            val = math.ceil(val / 3)
            heapq.heappush(heap, -1*val)
        return score