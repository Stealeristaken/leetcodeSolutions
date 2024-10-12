class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events= []
        for interval in intervals:
            events.append((interval[0],1))
            events.append((interval[1]+1,-1))
        events.sort(key=lambda x:(x[0],x[1]))
        concurrent, max_concurrent = 0, 0
        for event in events:
            concurrent += event[1]
            max_concurrent = max(max_concurrent,concurrent)
        return max_concurrent