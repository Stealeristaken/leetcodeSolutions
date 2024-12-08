import heapq
from typing import List 

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        ans = 0
        prev = 0 
        min_heap = [] 
        events.sort()
        for s, e, v in events:
            while(min_heap and s > min_heap[0][0]):
                prev = max(prev, heapq.heappop(min_heap)[1])
            ans = max(ans, prev + v)
            heapq.heappush(min_heap, (e, v))
        return ans