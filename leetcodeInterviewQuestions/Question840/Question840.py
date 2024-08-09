class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        row_range = 0
        column_range = 0
        
        while row_range < len(grid) - 2:
            matrix = []
            for i in range(row_range, row_range + 3):
                ar = []
                for j in range(column_range, column_range + 3):
                    ar.append(grid[i][j])
                matrix.append(ar)
            
            if self.magic_square(matrix):  # Check if the current matrix is a magic square
                count += 1
    
            if column_range < len(grid[0]) - 3:
                column_range += 1
            else:
                column_range = 0
                row_range += 1
        
        return count  # Return the total count of magic squares

    def magic_square(self, matrix: List[List[int]]) -> bool:
        row_1 = matrix[0][0] + matrix[0][1] + matrix[0][2]
        row_2 = matrix[1][0] + matrix[1][1] + matrix[1][2]
        row_3 = matrix[2][0] + matrix[2][1] + matrix[2][2]
        col_1 = matrix[0][0] + matrix[1][0] + matrix[2][0]
        col_2 = matrix[0][1] + matrix[1][1] + matrix[2][1]
        col_3 = matrix[0][2] + matrix[1][2] + matrix[2][2]
        diagonal_1 = matrix[0][0] + matrix[1][1] + matrix[2][2]
        diagonal_2 = matrix[0][2] + matrix[1][1] + matrix[2][0]
        
        # Check if all rows, columns, and diagonals have the same sum (and equal to 15)
        if (row_1 == row_2 == row_3 == 15 and
            col_1 == col_2 == col_3 == 15 and
            diagonal_1 == diagonal_2 == 15):
            # Check if the matrix contains all numbers from 1 to 9
            elements = set(matrix[i][j] for i in range(3) for j in range(3))
            return elements == set(range(1, 10))
        
        return False