class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        if target > matrix[-1][-1]:
            return False    # <-- #3

        row = matrix[bisect_left(matrix,
                  target, key = lambda x: x[-1])]   # <-- #1

        idx = bisect_left(row, target)              # <-- #2

        return row[idx] == target