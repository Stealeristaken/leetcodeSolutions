class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        n, dp = len(s), [0]
        maxWordLen = len(max(dictionary, key=len))
        for i in range(1, n + 1):
            dp.append(dp[-1] + 1)
            for j in range(i - 1, max(i - maxWordLen - 1, -1), -1):
                if s[j:i] in dictionary:
                    dp[i] = min(dp[i], dp[j])
        return dp[-1]


class Solution:
    def minExtraChar(self, s:str, dictionary: List[str]) -> int:
        max_val = len(s) + 1
        dp = [max_val] * (len(s) + 1)
        dp[0] = 0
        dictionary_set = set(dictionary)

        for i in range(1, len(s) + 1):
            dp[i] = dp[i - 1] + 1

            for l in range(1, i + 1):
                if s[i - l : i] in dictionary_set:
                    dp[i] = min(dp[i], dp[i - l])

        return dp[-1]