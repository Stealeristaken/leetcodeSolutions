class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        n = len(obstacleGrid[0])
        m = len(obstacleGrid)

        mat = [[0 for x in range(n + 1)] for x in range(m + 1)]
        mat[1][1] = 1

        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                if i == 1 and j == 1:
                    continue

                if obstacleGrid[i - 1][j - 1] == 1:
                    mat[i][j] == -1

                else:
                    left_nm = max(mat[i][j - 1], 0)
                    right_nm = max(mat[i - 1][j], 0)

                    mat[i][j] = left_nm + right_nm
        return mat[-1][-1]
