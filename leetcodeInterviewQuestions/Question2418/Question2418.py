class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n):
            heights[i] = [names[i], heights[i]]
        heights.sort(key=lambda x: x[1], reverse=True)
        for j in range(n):
            names[j] = heights[j][0]
        return names