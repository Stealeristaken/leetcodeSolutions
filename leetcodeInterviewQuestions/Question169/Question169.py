class Solution:
      def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
  
  
  
  
  ####################
import statistics
f = open("user.out", 'w')
for line in stdin:
    l = sorted(map(int, line.rstrip()[1:-1].split(',')))
    print(l[len(l) // 2], file=f)
exit(0)