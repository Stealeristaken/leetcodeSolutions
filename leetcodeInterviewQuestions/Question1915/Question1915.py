class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        orda = ord('a')
        mask = 0
        combs = {0:1}
        for w in word:
            mask ^= 1 << ord(w) - orda
            combs[mask] = combs.get(mask, 0) + 1

        ans = 0
        clist = list(combs)
        for i in range(len(combs)):
            i_res = combs[clist[i]]
            ans +=  i_res * (i_res - 1) // 2
            for j in range(i + 1, len(clist)):
                if (clist[i] ^ clist[j]).bit_count() == 1:
                    ans += i_res * combs[clist[j]]
        return ans