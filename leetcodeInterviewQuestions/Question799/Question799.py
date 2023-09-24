class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        result = [[0.0] * 101 for _ in range(101)]
        result[0][0] = poured
        for i in range(100):
            for j in range(i + 1):
                if result[i][j] >= 1:
                    result[i + 1][j] += (result[i][j] - 1) / 2.0
                    result[i + 1][j + 1] += (result[i][j] - 1) / 2.0
                    result[i][j] = 1.0
        return result[query_row][query_glass]