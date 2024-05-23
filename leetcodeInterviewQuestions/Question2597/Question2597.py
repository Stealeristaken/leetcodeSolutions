from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # brute force: generate all subsets . how to compare absolute difference? use an additional array of size 1000
        nums.sort()

        def dfsBack(i, subset, count):
            if i == len(nums):
                return 1 if len(subset) > 0 else 0
            
            subsetCount = 0
            
            # pick
            if nums[i] - k < 0 or count[nums[i] - k] == 0: # check if nums[i] - k exists in subset. this is why we have to SORT because we are always comparing the current number MINUS k, if we dont sort then we have to do current number PLUS k as well
                count[nums[i]] += 1
                subset.append(nums[i])
                subsetCount += dfsBack(i+1, subset, count)

                #backtrack
                subset.pop()
                count[nums[i]] -= 1

            # dont pick
            subsetCount += dfsBack(i+1, subset, count)

            return subsetCount

        return dfsBack(0, [], [0 for i in range(max(nums)+1)])
  
  
######################################
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        def dfs(i,tmp):
            if len(tmp) > 0:
                self.count += 1
            
            for j in range(i,len(nums)):
                if nums[j] - k not in tmp:
                    dfs(j + 1,tmp | {nums[j]})

        self.count = 0
        nums.sort()
        dfs(0,set())

        return self.count