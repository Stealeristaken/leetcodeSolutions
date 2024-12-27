from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxPrefix = max(values[0], values[1] + 1)
        res = values[0] + values[1] - 1
        for j, j_val in enumerate(values):
            if j == 0 or j == 1:
                continue

            option = maxPrefix + j_val - j
            if option > res:
                res = option
            
            maxPrefix = max(maxPrefix, j_val + j)

        return res