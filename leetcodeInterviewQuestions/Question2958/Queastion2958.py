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
  
  
  
############ Another Solution ############      


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = {}
        n = len(nums)

        left = 0
        right = left

        largest = 0

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] > k:
                largest = max(largest, right - left)
                while nums[left] != nums[right]:
                    counter[nums[left]] -= 1
                    left += 1
                counter[nums[left]] -= 1
                left += 1

            right += 1
        largest = max(largest, right - left)
        return largest