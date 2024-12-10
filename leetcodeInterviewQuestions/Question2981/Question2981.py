class Solution:
    def maximumLength(self, s: str) -> int:
        d = {}
        i = 0
        while i < len(s):
            length = 1
            while i < len(s) - 1 and s[i] == s[i+1]:
                length += 1
                i += 1
            a = d.get(s[i], [])
            a.append(length)
            d[s[i]] = a
            i += 1


        res = -1
        for a in d.values():
            a.sort()
            a.reverse()
            if len(a) > 2 and a[2] == a[1] and a[1] == a[0]:
                temp = a[0]
            elif len(a) > 1 and a[0] <= a[1] + 1 and a[0] > 1:
                temp = a[0] - 1
            elif a[0] > 2:
                temp = a[0] - 2
            else:
                temp = -1
            if temp > res:
                res = temp
        return res