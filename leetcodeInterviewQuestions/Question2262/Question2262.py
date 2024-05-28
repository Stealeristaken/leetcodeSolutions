from collections import defaultdict

class Solution:
    def appealSum(self, s):
        n, cur, dp = len(s), defaultdict(int), [0]

        for i in range(n):
            cur[s[i]] = i+1
            dp.append(dp[-1]+sum(cur.values()))

        return dp[-1]
  
  
  
class Solution:
    def appealSum(self, s: str) -> int:
        last_pos = [0] * 26  # Initialize last positions for a-z
        l = len(s)
        total = 0
        for idx, c in enumerate(s, 1):  # Start index from 1 for easier calculations
            cv = ord(c) - 97
            total += (idx - last_pos[cv]) * (l - idx + 1)
            last_pos[cv] = idx

        return total        