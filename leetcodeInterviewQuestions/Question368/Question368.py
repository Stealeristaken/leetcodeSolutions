from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        count = [1] * n
        prev_index = [-1] * n
        max_count, max_index = 0, -1

        nums.sort()

        for i in range(n):
            for j in reversed(range(i)):
                if nums[i] % nums[j] == 0 and count[i] < count[j] + 1:
                    count[i] = count[j] + 1
                    prev_index[i] = j
            if count[i] > max_count:
                max_count = count[i]
                max_index = i

        while max_index != -1:
            ans.append(nums[max_index])
            max_index = prev_index[max_index]

        return ans