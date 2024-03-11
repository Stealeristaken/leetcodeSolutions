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