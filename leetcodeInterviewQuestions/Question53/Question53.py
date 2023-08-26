class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result=-10000
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            if result<total:
                result=total
            if total<0:
                total=0
        return result