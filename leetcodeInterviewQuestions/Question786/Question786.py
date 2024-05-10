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
  
  
  
  
##################



class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def con(value):
            nb_smallest_fraction = 0
            numer = arr[0]
            denom = arr[-1]

            slow = 0
            for fast in range(1, len(arr)):
                while slow < fast and arr[slow] / arr[fast] < value:
                    if arr[slow] / arr[fast] > numer / denom:
                        numer, denom = arr[slow], arr[fast]

                    slow += 1

                nb_smallest_fraction += slow

            return nb_smallest_fraction, numer, denom

        l = arr[0] / arr[-1]
        r = 1

        while l < r:
            m = (l+r) / 2

            count, numer, denom = con(m)

            if count == k:
                return [numer, denom]

            if count > k:
                r = m
            else:
                l = m