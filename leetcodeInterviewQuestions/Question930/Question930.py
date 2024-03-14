class Solution:
      def numSubarraysWithSum(self, A: List[int], S: int) -> int:
          count = collections.Counter({0: 1})
          cur = res = 0
          for a in A:
              cur += a
              res += count[cur - S]
              count[cur] += 1
          return res
    
    