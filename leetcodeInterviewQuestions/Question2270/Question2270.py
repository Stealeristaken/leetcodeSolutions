from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        rsum = sum(nums)
        res = lsum = 0

        for i in range(len(nums) - 1):
            lsum += nums[i]
            rsum -= nums[i]
            if lsum >= rsum:
                res += 1
        return res