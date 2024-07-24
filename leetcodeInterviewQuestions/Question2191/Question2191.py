from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d={}
        for i,j in enumerate(mapping):
            d[i]= j
        d1 = []
        for i in nums:
            s = ''
            for j in str(i):
                s+=str(d[int(j)])
            d1.append((i,int(s)))
        d1 = sorted(d1,key=lambda x: x[1])
        d1 = [item[0] for item in d1]
        return d1   