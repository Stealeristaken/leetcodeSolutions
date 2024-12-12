import heapq
import math 
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-1 * i for i in gifts]
        heapq.heapify(gifts)
        for i in range(k):
            cur = -1 * heapq.heappop(gifts)
            heapq.heappush(gifts, -1 * math.floor(math.sqrt(cur)))
        return -1 * sum(gifts)