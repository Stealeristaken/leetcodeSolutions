from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        temp = 0
        for i in nums:
            temp ^= i
        temp ^= k
        return bin(temp).count('1')
  
  
  
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        n = len(nums)
        hasones = bool(max(nums) > 0)
        while k or hasones:
            numones = 0
            hasones = False
            for i in range(n):
                numones ^= (nums[i] % 2)
                nums[i] >>= 1
                if nums[i]:
                    hasones = True
            if numones != k % 2:
                ops += 1
            k >>= 1
        return ops