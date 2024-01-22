class Solution:
    def findErrorNumbers(self, nums: List[int])-> List[int]:
        dp=[0]*(len(nums))
        op=[]
        for i in range(len(nums)):
            if dp[nums[i]-1] != 1:
                dp[nums[i]-1] = 1

            else:
                op.append(nums[i])

        for i in range(len(dp)):
            if dp[i]==0:
                op.append(i+1)
        return op                


