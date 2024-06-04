from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        o, oc, e = 0, 0, 0
        for i in c.keys():
            if c[i]%2 == 0:
                e += c[i]
            else:
                oc += 1
                o += c[i] - 1
        if oc >= 1:
            o += 1
        return e + o