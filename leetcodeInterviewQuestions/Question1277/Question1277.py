class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        tot = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]:
                    if r - 1 >= 0 and c - 1 >= 0:
                        larger_cnt = min(matrix[r-1][c-1], matrix[r-1][c], matrix[r][c-1])
                    else:
                        larger_cnt = 0
                    
                    matrix[r][c] += larger_cnt 
                    tot += matrix[r][c]
            #print(matrix[r])
        return tot
  
  