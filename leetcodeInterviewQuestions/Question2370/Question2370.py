class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        d = {}
        ans = 1
        for i in range(len(s)):
            res = 1
            for j in range(k+1):
                if ord(s[i])-j in d:
                    res = max(res, d[ord(s[i])-j]+1)
                if ord(s[i])+j in d:
                    res = max(res, d[ord(s[i])+j]+1)
            d[ord(s[i])] = res
            ans = max(res, ans)
        return ans