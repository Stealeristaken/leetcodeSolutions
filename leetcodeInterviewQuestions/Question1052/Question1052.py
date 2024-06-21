from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        curSum = sum([customer for i, customer in enumerate(customers[:minutes]) if grumpy[i]])
        maxSum = curSum, 0, minutes
        for i in range(len(customers) - minutes):
            removed = customers[i]
            removed = removed if grumpy[i] else 0
            added = customers[i+minutes]
            added = added if grumpy[i+minutes] else 0
            curSum += added - removed
            if curSum > maxSum[0]:
                maxSum = curSum, i + 1, i + minutes + 1
        grumpy = grumpy[:maxSum[1]] + [0] * minutes + grumpy[maxSum[2]:]
        return sum([customer for i, customer in enumerate(customers) if not grumpy[i]])
  
  