class Solution:
    def heightChecker(self, heights: List[int]) -> int:       
        count_heights = 0
        expected = sorted(heights)
        for height in range(len(expected)):
            if expected[height] != heights[height]:
                count_heights+=1
        return count_heights