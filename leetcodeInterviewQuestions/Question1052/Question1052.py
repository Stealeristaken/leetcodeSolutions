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
  
########################## More memory efficient solution ##########################      

class Solution:
    def maxSatisfied(self, c: List[int], g: List[int], m: int) -> int:
        tot=0
        lc=len(c)
        for i in range(lc):
            if g[i]==0:
                tot+=c[i]
                c[i]=0
        t2=0
        for i in range(m):
            if c[i]>0:
                t2+=c[i]
        tmx=t2
        for i in range(1,lc-m+1):
            t2-=c[i-1]
            t2+=c[i+m-1]
            if t2>tmx:
                tmx=t2
        return tot+tmx