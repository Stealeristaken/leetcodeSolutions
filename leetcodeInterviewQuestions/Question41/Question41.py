class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        index=0
        while index<len(nums):
            if nums[index]!=index and nums[index]>=0 and nums[index]<len(nums) and nums[index]!=nums[nums[index]]:
                nums[nums[index]],nums[index]=nums[index],nums[nums[index]]
                continue

            index+=1


        index=1
        while index<len(nums):
            if index!=nums[index]:
                return index
            index+=1
        return nums[-1]+1
    
    
    
    
    
    
    
    #### # # # # #  another way to solve question 
    
    
    
f = open("user.out", 'w')
for line in stdin:
    s = set(map(int, line.rstrip()[1:-1].split(',')))
    ans = 1
    while ans in s:s
        ans += 1
    print(ans, file=f)
exit(0)