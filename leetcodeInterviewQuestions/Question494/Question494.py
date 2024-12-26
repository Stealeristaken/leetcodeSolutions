from collections import defaultdict
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            new_dp = defaultdict(int)
            for curr_sum in dp:
                new_dp[curr_sum + num] += dp[curr_sum]
                new_dp[curr_sum - num] += dp[curr_sum]
            dp = new_dp

        return dp[target]