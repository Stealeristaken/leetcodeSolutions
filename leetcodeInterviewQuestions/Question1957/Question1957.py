class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[:2]
        n = len(s)

        i = 2
        while i < n:
            if s[i] != ans[-1] or s[i] != ans[-2]:
                ans += s[i]
            
            i += 1
        
        return ans
     