class Solution:
    def minLength(self, s: str) -> int:
        n = len(s)
        if "AB" in s:
            for i in range(1, n):
                if s[i] == "B" and s[i-1] == "A":
                    s = s[0:i-1] + s[i+1:n]
                    return self.minLength(s)
        if "CD" in s:
            for i in range(1, n):
                if s[i] == "D" and s[i-1] == "C":
                    s = s[0:i-1] + s[i+1:n]
                    return self.minLength(s)
        return n