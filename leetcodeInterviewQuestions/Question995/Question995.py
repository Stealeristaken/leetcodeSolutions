from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        N = len(nums)
        total = 0
        arr = [0] * (N + 1)
        cur = 0
        for index, x in enumerate(nums):
            cur += arr[index]
            x ^= (cur % 2)
            if x == 0:
                if index + k - 1 >= N:
                    return -1
                cur += 1
                arr[index + k] -= 1
                total += 1 
        return total

        