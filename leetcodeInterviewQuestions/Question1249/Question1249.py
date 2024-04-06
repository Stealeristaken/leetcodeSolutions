class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        k = 0
        for i,v in enumerate(s):
            if v == '(':
                k += 1
            elif v == ')' and k == 0:
                s[i] = ''
            elif v == ')' and k >0:
                k -= 1
        j = 1
        for i in range(k):
            while s[-j] != '(':
                j += 1
            s[-j] = ''
        return ''.join(s)