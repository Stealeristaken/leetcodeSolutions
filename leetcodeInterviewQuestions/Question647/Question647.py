
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        i, ans = 0, 0
        while(i < n):
            j = i + 1
            while j < n and s[i] == s[j]:
                j += 1
            j -= 1
            for k in range(1, j - i + 1 + 1):
                ans += k
            k = 1
            while i - k >= 0 and j + k < n and s[i - k] == s[j + k]:
                ans += 1
                k += 1
            i = j
            i += 1
        return ans
