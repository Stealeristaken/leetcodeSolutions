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
  
  
  
  
  
  
##########################




import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(wage)
        workers = [(wage[i]/quality[i], quality[i]) for i in range(n)]
        workers.sort()
        total_quality = 0
        ratio = 0
        heap = []
        heapq.heapify(heap)
        for i in range(k):
            ratio = workers[i][0]
            total_quality += workers[i][1]
            heapq.heappush(heap, -workers[i][1])
        res = ratio*total_quality
        for i in range(k, n):
            ratio = workers[i][0]
            total_quality += workers[i][1]
            heapq.heappush(heap, -workers[i][1])
            quality = -heapq.heappop(heap)
            total_quality -= quality
            res = min(res, ratio*total_quality)
        return res