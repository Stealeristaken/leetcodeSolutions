class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        total_count=0
        dp=[{} for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff=nums[i]-nums[j]
                ending_at_j=dp[j].get(diff,0)
                dp[i][diff]=dp[i].get(diff,0)+ending_at_j+1
                total_count+=ending_at_j
        return total_count