from typing import List 
import heapq 

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
            projects = sorted(zip(capital, profits))
            max_heap = []
            current_capital = w
            index = 0
            for _ in range(k):
                  while index < len(projects) and projects[index][0] <= current_capital:
                        heapq.heappush(max_heap, -projects[index][1])
                        index += 1
                  if not max_heap:
                        break
                  current_capital += -heapq.heappop(max_heap)
            
            return current_capital  