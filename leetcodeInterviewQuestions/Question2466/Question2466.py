class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        f = [0] * (high+1)
        f[0] = 1

        for i in range(1, high+1):
            f[i] = (f[i-zero] + f[i-one]) % MOD
        
        res = 0
        for i in range(low, high+1):
            res += f[i]
        return res % MOD