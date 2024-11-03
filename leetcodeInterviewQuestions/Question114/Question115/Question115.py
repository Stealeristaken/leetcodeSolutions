class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for col in range(len(t)+1)] for row in range(len(s)+1)]
        for row in range(len(s)+1):
            dp[row][-1] = 1
        for row in range(len(s)-1, -1, -1):
            for col in range(len(t)-1, -1, -1):
                matched = s[row] == t[col]
                if matched:
                    dp[row][col] = dp[row+1][col] + dp[row+1][col+1]
                else:
                    dp[row][col] = dp[row+1][col]
        return dp[0][0]