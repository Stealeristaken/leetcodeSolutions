from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(1, len(nums) + 1):
            i = 1
            while x <= nums[len(nums) - i]:
                i += 1
                if len(nums) - i < 0:
                    break
            if x == i - 1:
                return x
        return -1