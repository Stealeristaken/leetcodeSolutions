from typing import List 


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        x = 0
        n = len(arr)
        d = {}
        d[0] = (0,-1,0)
        ans = 0
        for i in range(n):
            x ^= arr[i]
            if x in d:  
                cnt = d[x][2] + 1              
                total = d[x][0] + (i-d[x][1])*cnt
                ans += total - cnt
                d[x] = (total,i,cnt)
            else:
                d[x] = (0,i,0)

        return ans