from typing import List 

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:

        # Max outgoing nodes - max num
        city_roads_freq = [0] * n
        
        for city1, city2 in roads:
            city_roads_freq[city1] += 1
            city_roads_freq[city2] += 1

        ans = 0
        city_roads_freq.sort()
        for val, cnt in enumerate(city_roads_freq):
            ans += (val + 1) * cnt
        
        return ans
        
        
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        Arr = [0] * n  # i-th city has Arr[i] roads
        for A,B in roads:
            Arr[A] += 1 # Each road increase the road count
            Arr[B] += 1
        Arr.sort()  # Cities with most road should receive the most score
        summ = 0
        for i in range(len(Arr)):
            summ += Arr[i] * (i+1)  # Multiply city roads with corresponding score
        
        return summ