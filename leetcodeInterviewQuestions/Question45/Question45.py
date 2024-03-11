class Solution:
    def jump(self, nums: List[int]) -> int:
        currPos=0
        distance=0
        jumps=0
        for i in range(len(nums)-1):
            distance=max(distance,i+nums[i])
            if currPos==i:
                jumps+=1
                currPos=distance
        return (jumps)