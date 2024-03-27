class Solution:
      def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
  
  
  
  
  
############ Another Solution ############
from typing import List 

class Solution:
      def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
            # Solution 1: Brute Force
            # Time: O(n^2)
            # Space: O(1)

            # Solution 2: Sliding Window
            l, r = 0, 0
            ans = 0
            curProduct = 1
            # while r < len(nums):
            #     while l <= r and curProduct * nums[r] >= k:
            #         curProduct /= nums[l]
            #         ans += r - l
            #         l += 1

            #     curProduct *= nums[r]
            #     r += 1
            while r < len(nums):
                  curProduct *= nums[r]
            while l <= r and curProduct >= k:
                  curProduct /= nums[l]
                  l += 1
            ans += r - l + 1

            r += 1

            # while l < len(nums):
            #     ans += r - l
            #     l += 1

            return ans
