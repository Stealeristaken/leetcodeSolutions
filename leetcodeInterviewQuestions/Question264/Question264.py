nums = set([1])
while len(nums) < 4*1690:
    curr = nums.copy()
    for num in nums:
        curr.add(2*num)
        curr.add(3*num)
        curr.add(5*num)
    nums = curr
res = sorted(list(nums))

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        return res[n-1]