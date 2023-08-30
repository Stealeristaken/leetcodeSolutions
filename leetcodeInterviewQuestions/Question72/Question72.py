class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def solvation(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i] == word2[j]:
                dp[i][j] = solvation(i-1, j-1)
                return dp[i][j]
            else:
                insert = solvation(i, j-1)
                delete = solvation(i-1, j)
                update = solvation(i-1, j-1)

                result = 1 + min(insert, delete, update)
                dp[i][j] = result
                return result

        m, n = len(word1), len(word2)
        dp = [[-1] * (n + 1) for _ in range(m)]
        return solvation(m-1, n-1)
