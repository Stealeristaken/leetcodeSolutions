class Solution:
    def minSwaps(self, nums: list[int]) -> int:

        n, k = len(nums), sum(nums)
        mx = tally = sum(nums[:k])
        nums.extend(nums[:k])
        
        for num1, num2 in zip(nums[k:], nums):
            tally+= num1 - num2
            if tally > mx: mx = tally
        
        return k - mx
  
  
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        window_size = sum(nums)
        one_cnt = sum(nums[n-window_size:n])
        res = window_size-one_cnt
        for i in range(n-1, -1, -1):
            one_cnt += nums[i-window_size]-nums[i]
            res = min(res, window_size-one_cnt)
        return res