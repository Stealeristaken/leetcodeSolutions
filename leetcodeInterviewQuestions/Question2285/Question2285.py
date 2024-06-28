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
        