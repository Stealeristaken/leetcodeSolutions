import math
from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(maxPerStore):
            requiredStores = 0
            for quantity in quantities:
                requiredStores += (quantity + maxPerStore - 1) // maxPerStore  
            return requiredStores <= n
        low, high = 1, max(quantities)
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_distribute(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return result