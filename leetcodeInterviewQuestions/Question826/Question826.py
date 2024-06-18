from typing import List

class Solution:
    def maxProfitAssignment(self, d: List[int], profit: List[int], worker: List[int]) -> int:
        res = j = current_max = 0
        job = sorted(zip(d, profit))
        worker.sort()
        for w in worker:
            while j < len(job) and job[j][0] <= w:
                current_max = max(current_max, job[j][1])
                j += 1
            res += current_max
        return res