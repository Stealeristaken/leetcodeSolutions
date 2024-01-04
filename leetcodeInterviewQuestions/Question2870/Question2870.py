class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts={}
        for x in nums:
            counts[x]=counts.get(x,0)+1
            ans=0
        for x in counts:
            if counts[x]==1:
                return -1
            if counts[x]%3==0:
                ans+=counts[x]//3
            else:
                ans+=1+(counts[x]//3)
        return ans