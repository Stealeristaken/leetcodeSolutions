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