class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        champs = [1] * n

        for _, weaker_team in edges:
            if champs[weaker_team]:
                champs[weaker_team] = 0
                n -= 1
            if n == 1:
                return champs.index(1)

        return -1 if n >= 2 else champs.index(1)