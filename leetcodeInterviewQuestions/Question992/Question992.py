from collections import defaultdict

class Solution:
    def countSubarraysWithAtMostKDistinct(self, nums, k):
        n = len(nums)
        mp = defaultdict(int)
        i, j = 0, 0
        c = 0
        
        while j < n:
            mp[nums[j]] += 1
            
            while i <= j and len(mp) > k:
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                i += 1
            
            c += (j - i + 1)
            j += 1
        
        return c
    
    def subarraysWithKDistinct(self, nums, k):
        return self.countSubarraysWithAtMostKDistinct(nums, k) - self.countSubarraysWithAtMostKDistinct(nums, k - 1)
  
  
############ Another Solution ############



class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def f(counts=[0] * (len(nums) + 1), low=0, high=0, k=k):
            for num in nums:
                if not counts[num]:
                    if (k := k - 1) < 0:
                        counts[nums[high]] = 0
                        low = high = high + 1
                counts[num] += 1
                if k <= 0:
                    while counts[(a := nums[high])] > 1:
                        counts[a] -= 1
                        high += 1
                    yield high - low + 1

        return sum(f())  