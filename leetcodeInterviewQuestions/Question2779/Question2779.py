class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        intervals = [0] * (max(nums) + 2)

        for n in nums:
            intervals[max(n-k, 0)] += 1
            intervals[min(n+k+1, len(intervals)-1)] -= 1
        
        cur = 0
        res = 0
        for x in intervals:
            cur += x
            res = max(res, cur)
        
        return res