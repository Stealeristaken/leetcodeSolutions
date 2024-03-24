class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, _ in enumerate(nums):
            while(i+1 != nums[i]):
                n = nums[i]
                tmp = nums[n-1]
                if tmp == nums[i]:
                    return tmp
                else:
                    nums[i], nums[n-1] = nums[n-1], nums[i]
            i += 1
        return -1
    
    
    
    
############################################################################################################        

import sys 
from collections import Counter 
from json import loads 
stdin = open('user.in', 'r')
sys.stdout = open('user.out', 'w')
for nums in map(loads, stdin):
    print(Counter(nums).most_common(1)[0][0])
            