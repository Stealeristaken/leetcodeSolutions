class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x : x[0])
        merged=[]

        for i in intervals:
            if not merged or merged[-1][1]<i[0]:
                merged.append(i)

            else:
                merged[-1][-1]=max(merged[-1][-1],i[1])

        return merged
    
    
    
    
    
###### 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, n in enumerate(intervals):
            if newInterval[1] < n[0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > n[1]:
                res.append(n)

            else:
                newInterval = [min(newInterval[0], n[0]), max(newInterval[1], n[1])]

        res.append(newInterval)

        return res