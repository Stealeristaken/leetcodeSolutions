from typing import List

import heapq
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort(reverse=True)

        totalHappiness = 0
        for i in range(k):
            
            cur=max(happiness[i]-i,0)
            totalHappiness += cur
            # Decrement happiness of remaining children
            # for j in range(len(happiness)):
            #     happiness[j] = max(0, happiness[j] - 1)

        return totalHappiness
  
  
  
  
  ######################
  
  
  
  