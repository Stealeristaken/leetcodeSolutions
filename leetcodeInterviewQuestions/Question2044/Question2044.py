class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        prev = Counter()
        prev[0] = 1
        
        for elem in nums:
            max_or |= elem

            current = Counter()
            for prev_or, cnt in prev.items():
                current[prev_or | elem] += cnt
            prev.update(current)
        
        return prev[max_or]
    
##Time Complexity (TC): O(n * 2^n) Space Complexity (SC): O(2^n)