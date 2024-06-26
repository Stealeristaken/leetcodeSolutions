from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        res = 0
        def dfs(i, path):
            if i == len(nums):
                nonlocal res
                res += path
                return
            
            dfs(i+1, path)
            dfs(i+1, path ^ nums[i])
        
        dfs(0, 0)
        return res



# ---------------------------------------------------


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res |= num
        return res * (1 << (len(nums) - 1))