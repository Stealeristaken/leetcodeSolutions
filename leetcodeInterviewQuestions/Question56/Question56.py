class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda l: l[0])
        result=[intervals[0]]
        for i in range(1,len(intervals)):
            if result[-1][1]>=intervals[i][0]:
                result[-1][1]=max(intervals[i][1],result[-1][1])
            else:
                result.append(intervals[i])
        return result