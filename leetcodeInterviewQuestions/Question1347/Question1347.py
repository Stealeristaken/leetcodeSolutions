class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res=0
        for i in set(s):
            if s.count(i)>t.count(i):
                res+=s.count(i)-t.count(i)
        return res