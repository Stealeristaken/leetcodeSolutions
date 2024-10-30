class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)
        lds = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], lds[j] + 1)
        min_removals = n
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:
                mountain_length = lis[i] + lds[i] - 1
                min_removals = min(min_removals, n - mountain_length)
        return min_removals