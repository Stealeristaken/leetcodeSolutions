class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = start ^ goal
        ans = bin(x)
        count = 0
        for i in str(ans)[2:]:
            if i == '1':
                count += 1
        return count

        