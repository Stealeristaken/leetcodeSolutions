from typing import List 
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        final = {}
        ans = []
        dup = sorted(score, reverse = True)
        for i in range(len(dup)):
            final[dup[i]] = i+1
        for i in score:
            if final[i] > 3:
                ans.append(str(final[i]))
            else:
                if final[i] == 1:
                    ans.append("Gold Medal")
                elif final[i] == 2:
                    ans.append("Silver Medal")
                else:
                    ans.append("Bronze Medal")
        return ans
  
  
  
##############   ### 


import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        new=[i for i in range(len(score))]
        x=1
        for _ in range(len(score)):
            indx=score.index(max(score))
            score[indx]=-1
            if x==1:
                new[indx]='Gold Medal'
            elif x==2:
                new[indx]='Silver Medal'
            elif x==3:
                new[indx]='Bronze Medal'
            else:
                new[indx]=str(x)
            x+=1
        
        return new
        


        