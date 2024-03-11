"""
1st Solution by using lru_cache.

"""

class Solution:
  def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    jobs = sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)])

    for i in range(len(startTime)):
      startTime[i] = jobs[i][0]

    @functools.lru_cache(None)
    def dp(i: int) -> int:
      if i == len(startTime):
        return 0
      j = bisect.bisect_left(startTime, jobs[i][1])
      return max(jobs[i][2] + dp(j), dp(i + 1))

    return dp(0)

"""
Solution 2 Just for Fun
"""
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime,endTime,profit))
        cache = {}
        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            res = dfs(i+1)
            j = bisect.bisect(intervals,(intervals[i][1], -1, -1))
            cache[i] = res = max (res, intervals[i][2] + dfs(j))
            return res
        return dfs(0)