class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        ans_matrix = [[0 for i in range(n)] for _ in range(n)]

        for i in range(n):
            ans_matrix[0][i] = matrix[0][i]

        for row in range(1, n):
            for col in range(n):
                #if current value is starting of row
                if col == 0:
                    ans_matrix[row][col] = matrix[row][col] + min(ans_matrix[row-1][col], ans_matrix[row-1][col+1])

                #if current value is at the end of the current row
                elif col == n-1:
                    ans_matrix[row][col] = matrix[row][col] + min(ans_matrix[row-1][col], ans_matrix[row-1][col-1])

                #otherwise
                else:
                    ans_matrix[row][col] = matrix[row][col] + min(ans_matrix[row-1][col], min(ans_matrix[row-1][col+1], ans_matrix[row-1][col-1]))

        return min(ans_matrix[n-1])