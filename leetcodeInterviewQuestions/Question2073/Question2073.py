from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res =0 
        while tickets[k]:
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    break
                if  tickets[i] > 0:
                    tickets[i]-=1
                    res+=1            
        return res
  
  
  
#########

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(t, tickets[k]) for t in tickets[:k]) + tickets[k] + sum(min(t, tickets[k] - 1) for t in tickets[k+1:])