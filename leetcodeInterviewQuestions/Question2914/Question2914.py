class Solution:
    def minChanges(self, s: str) -> int:
        c = 0
        for i in range(0, len(s), 2):
            a = s[i:i+2]
            if a == "01" or a == "10":
                c += 1
        return c