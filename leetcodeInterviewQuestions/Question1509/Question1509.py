from typing import List

def minDifference(nums):
    if len(nums) <= 4:
        return 0
    nums.sort()
    #mi = float("inf") 
    return min(
        nums[-1] - nums[3],  
        nums[-2] - nums[2], 
        nums[-3] - nums[1],  
        nums[-4] - nums[0]   
    )

f = open('user.out','w')
for i in map(loads,stdin):
    f.write(f'{minDifference(i)}\n') 
f.flush()
exit(0)
        