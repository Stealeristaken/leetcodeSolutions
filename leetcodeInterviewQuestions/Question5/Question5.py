class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        l = 0
        r = 1

        while r <= len(s):
            if s[l:r] != s[l:r][::-1]:
                if l > 0 and s[l - 1:r] == s[l - 1:r][::-1]:
                    l -= 1
                else:
                    while l < r and s[l:r] != s[l:r][::-1]:
                        l += 1
            res = s[l:r] if len(res) < len(s[l:r]) else res
            r += 1
        return res