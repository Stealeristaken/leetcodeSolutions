class Solution:
      def numSubarraysWithSum(self, A: List[int], S: int) -> int:
          count = collections.Counter({0: 1})
          cur = res = 0
          for a in A:
              cur += a
              res += count[cur - S]
              count[cur] += 1
          return res
    
######     More Variants of the Problem     ######    

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        i = count = res = 0
        for j in range(len(nums)):
            if nums[j] == 1:
                goal -= 1
                count = 0
                      
            while goal == 0 and i <= j:
                goal += nums[i]
                i += 1
                count += 1
                if i > j - goal + 1:
                    break
                    
            while goal < 0:
                goal += nums[i]
                i += 1

            res += count
        return res