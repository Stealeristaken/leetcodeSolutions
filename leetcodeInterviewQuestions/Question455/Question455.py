class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()
        res = 0  # track number of satisfied children
        for val in s:
            if res == len(g):
                break
            if g[res] <= val:
                res += 1
        return res