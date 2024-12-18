from typing import List 

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        ans = prices[:]
        stack = []

        for i, val in enumerate(prices):
            while stack and prices[stack[-1]] >= val:
                ans[stack.pop()] -= val
            stack.append(i)
        return ans