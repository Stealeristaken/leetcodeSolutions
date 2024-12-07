from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        
        def canAchievePenalty(P: int) -> bool:
            operations = 0
            for balls in nums:
                if balls > P:
                    operations += (balls - 1) // P
                if operations > maxOperations:
                    return False
            return operations <= maxOperations
        
        while left < right:
            mid = (left + right) // 2
            if canAchievePenalty(mid):
                right = mid
            else:
                left = mid + 1
        
        return left