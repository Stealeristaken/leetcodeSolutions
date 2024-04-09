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