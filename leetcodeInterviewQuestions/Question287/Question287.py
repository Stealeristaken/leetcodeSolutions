class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, _ in enumerate(nums):
            while(i+1 != nums[i]):
                n = nums[i]
                tmp = nums[n-1]
                if tmp == nums[i]:
                    return tmp
                else:
                    nums[i], nums[n-1] = nums[n-1], nums[i]
            i += 1
        return -1