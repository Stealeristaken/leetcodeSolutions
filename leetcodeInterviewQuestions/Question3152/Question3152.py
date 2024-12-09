from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        runningSum = 0
        partialSum = []
        oddEven = None

        for num in nums:
            if num % 2 == oddEven:
                runningSum += 1
            oddEven = num % 2
            partialSum.append(runningSum)

        out = []

        for start, end in queries:
            if partialSum[start] == partialSum[end]:
                out.append(True)
            else:
                out.append(False)
        return out