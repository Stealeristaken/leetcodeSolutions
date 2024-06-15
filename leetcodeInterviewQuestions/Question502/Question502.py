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
      
      
######################


def findMaximizedCapital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    if w > max(capital):
        return w + sum(nlargest(k, profits))
    maxProfit = []
    minCapital = [(c, p) for c, p in zip(capital, profits)]
    heapify(minCapital)
    
    for i in range(k):

        while minCapital and minCapital[0][0] <= w :
            c, p = heappop(minCapital)
            heappush(maxProfit, -1 * p)

        if not maxProfit :
            break
        w += -1 * heappop(maxProfit)

    return w

    
if __name__ =='__main__' :
    with open('user.out', 'w') as f :
        for k, w, profits, capital in zip(map(loads, stdin), map(loads, stdin), map(loads, stdin), map(loads, stdin)) :
            print(findMaximizedCapital(k, w, profits, capital), file = f)
    exit()