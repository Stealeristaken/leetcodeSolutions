from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def solve(i, curr):
            if i >= len(nums):
                ans.append(curr.copy())
                return
            curr.append(nums[i])
            solve(i+1, curr)

            curr.pop()
            solve (i+1, curr)
        solve(0,[])
        return ans
    
    
######

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res