from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        arr = sorted((nums[i], i) for i in range(len(nums)))
        visited, result, n = set(), 0, len(nums)
        for score, index in arr:
            if index in visited:
                continue
            visited.add(index - 1)
            visited.add(index + 1)
            visited.add(index)
            result += score
        return result