class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        prefix_sum=[nums[0]]
        for num in nums[1:]:
            prefix_sum.append(prefix_sum[-1]+num)
        max_len = -1 
        for i in range(1, n-1):
            if prefix_sum[i]>nums[i+1]:
                max_len=prefix_sum[i+1]
                
        return max_len        

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        
        while 1:
            if not nums: return -1
            
            maxx = max(nums)
            suma = sum(nums) - maxx
            
            if suma<=maxx: nums.remove(maxx)
            else: break
                
                
        return sum(nums)
                
        

