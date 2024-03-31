class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        l = 0
        r = 0
        min_k_idx = None
        max_k_idx = None
        n = len(nums)
        count = 0

        while r < n:
            # processing number at r
            if nums[r] == minK:
                min_k_idx = r
            if nums[r] == maxK:
                max_k_idx = r
            
            # shrinking / skipping if needed
            if nums[r] > maxK or nums[r] < minK:
                l = r + 1
                r = r + 1
                min_k_idx = None
                max_k_idx = None
            else:
                # calculating count
                if max_k_idx is not None and min_k_idx is not None: # if both are found

                    if max_k_idx > min_k_idx: #if the last one we found was a maxK
                        count += min_k_idx - l + 1
                    else: # if the last one we found was a minK, or if maxK = minK
                        count += max_k_idx - l + 1
                
                # incrementing r 
                r += 1
        
        return count