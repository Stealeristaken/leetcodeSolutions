class Solution:
    def compressedString(self, word: str) -> str:
        d = '0123456789'
        ans = []
        count = 0
        cur = ''
        for c in word:
            if c != cur:
                if count >= 9:
                    ans.append((f"9{cur}")*(count//9))
                    count %= 9
                if count:
                    ans.append(d[count] + cur)
                count = 1
                cur = c
            else:
                count += 1
        if count >= 9:
            ans.append((f"9{cur}")*(count//9))
            count %= 9
        if count:
            ans.append(d[count] + cur)
        return "".join(ans)