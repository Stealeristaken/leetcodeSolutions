class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # def helper(r,k):
        #     if k == len(key):
        #         return 0
        #     res = float('inf')
        #     for i in range(len(ring)):
        #         if ring[x] == key
        dp = {}
        def rec(k,p):
            if k >= len(key):
                return 0
            if (k,p) in dp:
                return dp[(k,p)]
            ans =float('inf')

            for x in range(len(ring)):
             
                if ring[x]== key[k]:
                    min_dist = min(abs(p-x),abs(len(ring)-abs(p-x)))
            
                    ans = min(ans,min_dist+rec(k+1,x))
            dp[(k,p)] =ans+1        
            return ans+1
        return rec(0,0)
        