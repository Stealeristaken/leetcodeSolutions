class Solution:
    def minSwaps(self, nums: list[int]) -> int:

        n, k = len(nums), sum(nums)
        mx = tally = sum(nums[:k])
        nums.extend(nums[:k])
        
        for num1, num2 in zip(nums[k:], nums):
            tally+= num1 - num2
            if tally > mx: mx = tally
        
        return k - mx