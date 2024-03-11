class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, curr):
            if not nums:
                res.append(curr)
            for i in set(nums):
                rem=list(nums)
                rem.remove(i)
                dfs(rem,curr+[i])
        res=[]
        dfs(nums,[])
        return res