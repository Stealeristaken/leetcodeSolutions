from typing import List 
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_stack, max_stack = deque([]), deque([])
        l, res = 0, 0
        if not nums or len(nums) == 0:
            return 0
        for r, num in enumerate(nums):
            while min_stack and min_stack[-1][1] >= num:
                min_stack.pop()
            min_stack.append((r, num))
            while max_stack and max_stack[-1][1] <= num:
                max_stack.pop()
            max_stack.append((r, num))
            while max_stack[0][1] - min_stack[0][1] > limit:
                if l >= min_stack[0][0]:
                    min_stack.popleft()
                if l >= max_stack[0][0]:
                    max_stack.popleft()
                l += 1
            res = max(res, r - l + 1)
        return res
  
  