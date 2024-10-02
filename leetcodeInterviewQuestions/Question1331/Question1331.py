from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = [n for n in set(arr)]
        nums.sort()
        ordering = {}
        for i in range(len(nums)):
            ordering[nums[i]] = i + 1
        
        for i in range(len(arr)):
            arr[i] = ordering.get(arr[i])

        return arr
        