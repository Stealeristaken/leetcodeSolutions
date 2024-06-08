from typing import List 

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        st = set()
        curr,last = 0,0
        if len(nums) == 1:
            return False
        if k == 1:
            return True
        for i in nums:
            curr += i
            if curr%k in st:
                return True
            else:
                st.add(last)
                last = curr%k
        print(curr)
        return False
