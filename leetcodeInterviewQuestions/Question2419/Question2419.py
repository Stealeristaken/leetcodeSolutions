class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        output, cur = 0, 0
        for i in nums:
            if i == m:
                cur += 1
                output = max(output, cur)
            else:
                cur = 0
        return output