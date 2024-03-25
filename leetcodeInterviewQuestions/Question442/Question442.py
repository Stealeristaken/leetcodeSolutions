class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
            res = []
            for i in range(len(nums)):
                  if nums[abs(nums[i])-1] < 0:
                   res.append(abs(nums[i]))
                  else:
                   nums[abs(nums[i])-1] *= -1
            return res
      
      
      
########### MAP SOLUTION ################

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicatemap={}
        for i in nums:
            if(i in duplicatemap):
                duplicatemap[i]+=1
            else:
                duplicatemap[i]=1
        return [k for k,v in duplicatemap.items() if v>=2]
            
            
        