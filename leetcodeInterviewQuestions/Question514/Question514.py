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
        
        
        

class Solution:
    def findRotateSteps(self, s: str, t: str) -> int:
        s = [ord(c) - ord('a') for c in s]
        t = [ord(c) - ord('a') for c in t]
        n, m = len(s), len(t)

        pos = [0] * 26 
        for i, c in enumerate(s):
            pos[c] = i
   
        left = [None] * n
        for i, c in enumerate(s):
            left[i] = pos[:]
            pos[c] = i  


        pos = [0] * 26  
        for i in range(n - 1, -1, -1):
            pos[s[i]] = i
        
        right = [None] * n
        for i in range(n - 1, -1, -1):
            right[i] = pos[:]
            pos[s[i]] = i 

        pos = [[] for _ in range(26)]
        for i, b in enumerate(s):
            pos[b].append(i)

        f = [0] * n
        for j in range(m - 1, 0, -1):
            c = t[j]
            if c == t[j - 1]:
                continue
            nf = [0] * n
            for i in pos[t[j - 1]]:
                l, r = left[i][c], right[i][c]
                res1 = f[l] + (n - l + i if l > i else i - l)
                res2 = f[r] + (n - i + r if r < i else r - i)
                if res2 < res1 : res1 = res2
                nf[i] = res1          
            f = nf
        if s[0] == t[0]:
            return f[0] + m
        c = t[0]
        l, r = left[0][c], right[0][c]
        return min(f[l] + n - l, f[r] + r) + m