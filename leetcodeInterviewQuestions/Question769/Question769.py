from collections import defaultdict
import math

class Solution:
    def maxChunksToSorted(self, nums):
        len_nums = len(nums)

        ret_val = 0
        max_num = -math.inf
        
        i = 0
        while (i < len_nums):
            num = nums[i]

            max_num = max(max_num, num)
            if (max_num == i):
                ret_val += 1

            i += 1

        return ret_val