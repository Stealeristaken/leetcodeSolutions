# Question 10 - Regular Expression Matching

class Solution(object):
    def isMatch(self, s, p):
        dp = [[False] * (len(s) + 1) for i in range(len(p) + 1)]

        dp[0][0] = True

        for i in range(1, len(dp)):
            if p[i - 1] == '*' and i > 1:
                dp[i][0] = dp[i - 2][0]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):

                if p[i - 1] == s[j - 1] or p[i - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                if p[i - 1] == '*':
                    if p[i - 2] == '.' or p[i - 2] == s[j - 1]:
                        dp[i][j] = dp[i - 2][j] or dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 2][j]

        return dp[-1][-1]