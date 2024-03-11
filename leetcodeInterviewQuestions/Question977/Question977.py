class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i**2 for i in nums])
        
        
        
        
#Faster time complexity


sys.stdout = open('user.out', 'w')

for nums in map(loads, sys.stdin):
    result = sorted(x**2 for x in nums)
    print(dumps(result).replace(' ', ''))
exit()