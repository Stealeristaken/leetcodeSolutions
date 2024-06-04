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
  
  
###############

class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss = set()
        for letter in s:
            if letter not in ss:
                ss.add(letter)
            else:
                ss.remove(letter)
        if len(ss) != 0:
            return len(s) - len(ss) + 1
        else:
            return len(s)
        