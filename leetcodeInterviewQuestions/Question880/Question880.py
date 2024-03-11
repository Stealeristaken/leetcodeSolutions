class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        a = [1]
        for x in s[1:]:
            if a[-1] >= k:
                break
            if x.isdigit():
                a.append(a[-1] * int(x))
            else:
                a.append(a[-1] + 1)
        for i in reversed(range(len(a))):
            k %= a[i]
            if not k and s[i].isalpha():
                return s[i]
