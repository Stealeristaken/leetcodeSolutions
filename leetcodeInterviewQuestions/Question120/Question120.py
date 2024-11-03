class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = triangle.pop(0)
        while triangle:
            cur = triangle.pop(0)
            prev.insert(0,20000)
            prev.append(20000)
            prev.append(20000)
            for i in range(len(cur)):
                mini = min(prev[i],prev[i+1])
                cur[i]+=mini
            prev = cur        
        return min(prev)