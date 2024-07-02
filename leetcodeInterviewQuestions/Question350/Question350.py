from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h1={}
        for i in nums1:
            if i in h1:
                h1[i]+=1
            else:
                h1[i]=1
        res=[]
        for i in nums2:
            if i in h1:
                res.append(i)
                if h1[i]==1:
                    del h1[i]
                else:
                    h1[i]-=1
        return res