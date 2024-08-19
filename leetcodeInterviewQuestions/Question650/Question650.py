class Solution:
    def minSteps(self, n: int) -> int:
        a = 1
        min_steps = 0
        a_copied = 0
        while a < n:
            if n % a == 0:
                a_copied = a
                min_steps += 1
            min_steps += 1
            a += a_copied
        return min_steps