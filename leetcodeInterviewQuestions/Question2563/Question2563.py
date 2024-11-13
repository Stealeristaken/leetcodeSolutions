class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def dfs(x):
            nums.sort()
            i,j,count = 0,len(nums)-1,0 
            while i < j:
                val = nums[i] + nums[j]
                if val <= x:
                    count += j-i
                    i += 1 
                else:
                    j -= 1 
            return count 
        return dfs(upper) - dfs(lower-1)