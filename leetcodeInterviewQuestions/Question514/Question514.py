class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # def helper(r,k):
        #     if k == len(key):
        #         return 0
        #     res = float('inf')
        #     for i in range(len(ring)):
        #         if ring[x] == key
        dp = {}
        def rec(k,p):
            if k >= len(key):
                return 0
            if (k,p) in dp:
                return dp[(k,p)]
            ans =float('inf')

            for x in range(len(ring)):
             
                if ring[x]== key[k]:
                    min_dist = min(abs(p-x),abs(len(ring)-abs(p-x)))
            
                    ans = min(ans,min_dist+rec(k+1,x))
            dp[(k,p)] =ans+1        
            return ans+1
        return rec(0,0)
        
        
        
# https://space.bilibili.com/206214
class Solution:
    def findRotateSteps(self, s: str, t: str) -> int:
        s = [ord(c) - ord('a') for c in s]
        t = [ord(c) - ord('a') for c in t]
        n, m = len(s), len(t)

        # 先算出每个字母的最后一次出现的下标
        # 由于 s 是环形的，循环结束后的 pos 就刚好是 left[0]
        pos = [0] * 26  # 初始值不重要
        for i, c in enumerate(s):
            pos[c] = i
        # 计算每个 s[i] 左边 a-z 的最近下标（左边没有就从 n-1 往左找）
        left = [None] * n
        for i, c in enumerate(s):
            left[i] = pos[:]
            pos[c] = i  # 更新下标

        # 先算出每个字母的首次出现的下标
        # 由于 s 是环形的，循环结束后的 pos 就刚好是 right[n-1]
        pos = [0] * 26  # 初始值不重要
        for i in range(n - 1, -1, -1):
            pos[s[i]] = i
        # 计算每个 s[i] 右边 a-z 的最近下标（左边没有就从 0 往右找）
        right = [None] * n
        for i in range(n - 1, -1, -1):
            right[i] = pos[:]
            pos[s[i]] = i  # 更新下标

        pos = [[] for _ in range(26)]
        for i, b in enumerate(s):
            pos[b].append(i)

        f = [0] * n
        for j in range(m - 1, 0, -1):
            c = t[j]
            if c == t[j - 1]:
                continue
            nf = [0] * n
            for i in pos[t[j - 1]]:
                l, r = left[i][c], right[i][c]
                res1 = f[l] + (n - l + i if l > i else i - l)
                res2 = f[r] + (n - i + r if r < i else r - i)
                if res2 < res1 : res1 = res2
                nf[i] = res1          
            f = nf
        if s[0] == t[0]:
            return f[0] + m
        c = t[0]
        l, r = left[0][c], right[0][c]
        return min(f[l] + n - l, f[r] + r) + m