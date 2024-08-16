class Solution(object):
    def maxDistance(self, arrays):
        small=arrays[0][0]
        big=arrays[0][-1]
        maxdist=0
        for i in range(1,len(arrays)):
            arr=arrays[i]
            maxdist=max(maxdist,abs(arr[-1]-small),abs(big-arr[0]))
            small=min(small,arr[0])
            big=max(big,arr[-1])
        return maxdist
  
  
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mn1, mn2 = float('inf'), float('inf')
        mx1, mx2 = float('-inf'), float('-inf')
        for i in arrays:
            mn, mx = i[0], i[-1]
            if mn < mn1:
                mn2, mn1 = mn1, mn
            elif mn < mn2:
                mn2 = mn
            if mx > mx1:
                mx2, mx1 = mx1, mx
            elif mx > mx2:
                mx2 = mx
        if mx1 == mx2 or mn1 == mn2:
            return mx1 - mn1
        for i in arrays:
            if (i[0], i[-1]) == (mn1, mx1):
                return max(abs(mx2 - mn1), abs(mx1 - mn2))
        return mx1 - mn1