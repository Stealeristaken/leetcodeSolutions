from typing import List
from sortedcontainers import SortedList
class Solution:

    def get_count(self, sorted_list, ele):
        lo = sorted_list.bisect(ele)
        hi = len(sorted_list) - lo
        return lo, hi

    def numTeams(self, rating: List[int]) -> int:
        left, right = SortedList(), SortedList(rating)
        res = 0
        for x in rating:
            right.remove(x) # process all right elements -> removing the left element
            lo_L, hi_L = self.get_count(left, x)
            lo_R, hi_R = self.get_count(right, x)
            res += (lo_L * hi_R) + (hi_L * lo_R)
            left.add(x)
        return res
