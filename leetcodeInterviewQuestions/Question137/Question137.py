class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n//3+1):
            if 3*i+1 == n or nums[3*i] != nums[3*i+1]:
                return nums[3*i]