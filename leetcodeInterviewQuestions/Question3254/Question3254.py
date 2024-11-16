from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        results = []
        
        for i in range(len(nums) - k + 1):
            subarray = nums[i:i + k]
            if subarray == sorted(subarray) and len(set(subarray)) == k and subarray[-1] - subarray[0] == k - 1:
                results.append(max(subarray))
            else:
                results.append(-1)
                
        return results