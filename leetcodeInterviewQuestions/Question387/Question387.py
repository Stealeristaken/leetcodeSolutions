class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if i == 0:
                if s[i] not in s[i+1:]:
                    return i
            elif i == len(s) - 1:
                if s[i] not in s[:len(s) - 1]:
                    return i
            else:
                if s[i] not in (s[0:i] + s[i+1:]):
                    return i
        return -1
        