class Solution:
    def bestClosingTime(self, customers: str) -> int:
        maxScore=score=0
        bestHour=-1

        for i, c in enumerate(customers):
            score+=1 if c=='Y' else -1
            if maxScore<score:
                maxScore, bestHour = score, i

        return bestHour+1