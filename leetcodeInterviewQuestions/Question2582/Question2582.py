class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        time = time % ((n - 1) * 2)

        position = 1 + time

        if position > n:
            position = n - (position - n)

        return position