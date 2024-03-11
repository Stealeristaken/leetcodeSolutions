class Solution(object):
    def isSubsequence(self, s, t):
        # Base case
        if not s:
            return True
        i = 0
        # Traverse elements of t string
        for j in t:
            # If this index matches to the index of s string, increment i pointer...
            if j == s[i]:
                i += 1
            # If the pointer is equal to the size of s...
            if i == len(s):
                break
        return i == len(s)