class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = collections.Counter()
        j = res = 0
        for i, num in enumerate(nums):
            cnt[num] += 1
            while cnt[num] > k and j < i:
                cnt[nums[j]] -= 1
                j += 1
            res = max(res, i - j + 1)
        return res