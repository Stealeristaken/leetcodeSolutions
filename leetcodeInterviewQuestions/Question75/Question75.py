class Solution:
    def sortColors(self, nums: List[int]) -> None:
        k1 = -1
        k2 = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                if k1 != -1 and k1 < n:
                    nums[k1], nums[i] = nums[i], nums[k1]
                    k1 += 1
                if k2 < n:
                    nums[k2], nums[i] = nums[i], nums[k2]
                    k2 += 1
            elif nums[i] == 1:
                if k1 == -1:
                    k1 = k2
                if k2 < n:
                    nums[k2], nums[i] = nums[i], nums[k2]
                    k2 += 1