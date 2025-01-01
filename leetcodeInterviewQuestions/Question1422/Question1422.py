class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        max_score = 0

        prefix_ones = [0] * n
        prefix_ones[0] = 1 if s[0] == '1' else 0
        for i in range(1, n):
            prefix_ones[i] = prefix_ones[i - 1] + (1 if s[i] == '1' else 0)

        zeros_count = 0
        for i in range(n - 1):  
            if s[i] == '0':
                zeros_count += 1
            ones_count = prefix_ones[n - 1] - prefix_ones[i]  
            max_score = max(max_score, zeros_count + ones_count)

        return max_score