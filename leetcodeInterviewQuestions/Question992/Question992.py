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