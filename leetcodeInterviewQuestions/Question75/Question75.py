from typing import List

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
                    
                    



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start,mid,end=0,0,len(nums)-1
    
        while mid<=end:
            if nums[mid]==0:
                nums[start],nums[mid]=nums[mid],nums[start]
                mid+=1
                start+=1
            elif nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                nums[mid],nums[end]=nums[end],nums[mid]
                end-=1

        