class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "": return ""

        have = 0
        needmap = {}
        havemap = {}

        res = float('inf')
        resl = [0, len(s)]

        for i in t:
            needmap[i] = 1 + needmap.get(i, 0)

        need = len(needmap)

        l = 0

        for r in range(len(s)):

            havemap[s[r]] = 1 + havemap.get(s[r], 0)

            if s[r] in needmap and havemap[s[r]] == needmap[s[r]]:
                have += 1

            while have == need:

                if (r - l + 1) < res:
                    res = r - l + 1
                    resl = [l, r]

                havemap[s[l]] -= 1

                if s[l] in needmap and havemap[s[l]] < needmap[s[l]]:
                    have -= 1

                l += 1

        l, r = resl

        return s[l:r + 1] if res != float('inf') else ""
    
    
    
    ###########
    # 2nd solution
    ###########
    class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        needstr = collections.defaultdict(int)
        for ch in t:
            needstr[ch] += 1
        needcnt = len(t)
        res = (0, float('inf'))
        start = 0
        for end, ch in enumerate(s):
            if needstr[ch] > 0:
                needcnt -= 1
            needstr[ch] -= 1
            if needcnt == 0:
                while True:
                    tmp = s[start]
                    if needstr[tmp] == 0:
                        break
                    needstr[tmp] += 1
                    start += 1
                if end - start < res[1] - res[0]:
                    res = (start, end)
                needstr[s[start]] += 1
                needcnt += 1
                start += 1
        return '' if res[1] > len(s) else s[res[0]:res[1]+1]
    
    ###########
    