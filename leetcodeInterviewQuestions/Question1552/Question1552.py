from typing import List 
# O(NlogN) solution

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            last_position, balls = position[0], 1
            for i in range(1, len(position)):
                if position[i] - last_position >= mid:
                    last_position = position[i]
                    balls += 1
            if balls >= m:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

      
class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def check(minmax):
            rem = m - 1
            lim = position[0] + minmax
            for p in position[1:]:
                if p >= lim:
                    rem -= 1
                    lim = p + minmax
            return rem <= 0

        position.sort()
        if m == 2:
            return position[-1] - position[0]
        low = 1
        high = (position[-1] - position[0]) // (m - 1)
        while low < high:
            mid = (low + high + 1) // 2
            if check(mid):
                low = mid
            else:
                high = mid -1
        return low        