class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        count=0
        n=len(nums)
        for i in range(n):
          if (nums[i]^k)>nums[i]:
            count=count+1
        sum=0
        for i in range(n):
          sum+=max(nums[i],nums[i]^k)
        if count%2==1:
          minus=1000000000
          for edge in edges:
            edge[0]=nums[edge[0]]
            edge[1]=nums[edge[1]]
            tmp=max(edge[0],edge[0]^k)+max(edge[1],edge[1]^k)
            if ((edge[0]^k)>edge[0] and (edge[1]^k)>edge[1]) or ((edge[0]^k)<edge[0] and (edge[1]^k)<edge[1]):
              edge[0]^=k
            minus=min([minus,tmp-(edge[0]^k)-(edge[1]^k),tmp-edge[1]-edge[0]])
          sum-=minus
        return sum
