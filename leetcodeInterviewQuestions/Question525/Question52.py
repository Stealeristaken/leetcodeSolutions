from typing import List
from json import loads
import sys
from sys import stdin

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = {0: -1}  # Initialize count dictionary with 0 at index -1
        max_length = 0
        balance = 0

        for i, num in enumerate(nums):
            if num == 0:
                balance -= 1
            else:
                balance += 1

            if balance in count:
                max_length = max(max_length, i - count[balance])
            else:
                count[balance] = i

        return max_length
  
  
  
###### sys.out solution as usual ######


sys.stdout = open('user.out', 'w')
for nums in map(loads, stdin):
    totalsum,hashmap=0,{0:-1}
    res,diff=0,0
    for i in range(len(nums)):
        if(nums[i]==0):
            totalsum-=1
        else:
            totalsum+=1
        try:
            diff=i-hashmap[totalsum]
            if(diff>res):
                res=diff
        except:
            hashmap[totalsum]=i
    print(res)