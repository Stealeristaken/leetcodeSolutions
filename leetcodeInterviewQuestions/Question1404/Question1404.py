class Solution:
    def numSteps(self, s: str) -> int:
        c = 0
        num = int(s, 2)
        while num != 1:
            if num % 2 == 1:
                num += 1
            else:
                num //= 2
            c += 1
        return c