class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        nums.sort()
        ans = []

        for i in range(0, len(nums), 3):
            if (nums[i+2]-nums[i]>k):
                return []
            else:
                ans.append([nums[i],nums[i+1],nums[i+2]])

        return ans        
  
  
  
  # Faster and Better Solution:
class Solution:
      def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        a=sorted(nums)
        b=max(i-j for i,j in zip(a[2::3],a[::3]))
        if b>k:
            return []
        return zip(a[::3],a[1::3],a[2::3])