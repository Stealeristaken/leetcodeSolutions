from collections import defaultdict

class Solution:
    def appealSum(self, s):
        n, cur, dp = len(s), defaultdict(int), [0]

        for i in range(n):
            cur[s[i]] = i+1
            dp.append(dp[-1]+sum(cur.values()))

        return dp[-1]