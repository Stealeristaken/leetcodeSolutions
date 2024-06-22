from typing import List 
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count_map = defaultdict(int)

        odd_count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd_count += 1
                nums[i] = odd_count
            count_map[odd_count] += 1

        res = count_map[k]
        for cnt in count_map:
            if (cnt + k) in count_map:
                res += count_map[cnt] * count_map[cnt+k]
        
        return res

###### O(N) solution ######

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        z=0
        start=0
        ans=0
        c=0
        for i in range(len(nums)):
            c+=nums[i]%2
            while start<i and (nums[start]%2==0 or c>k):
                if nums[start]%2:
                    z=0
                else:
                    z+=1
                c-=nums[start]%2
                start+=1
            if c==k:ans+=(z+1)
        return ans

def solve():
    f = open('user.out', 'w')
    iterator = map(loads, stdin)
    while True:
        try:
            nums = next(iterator)
            k = next(iterator)
        except StopIteration:
            break

        print(solution.numberOfSubarrays(nums, k), file=f)

solution = Solution()
solve()
exit()