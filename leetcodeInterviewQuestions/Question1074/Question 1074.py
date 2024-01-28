class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        count = 0
        rows, cols = len(matrix), len(matrix[0])
        
        # Calculate the cumulative sum for each row
        for row in matrix:
            for j in range(1, cols):
                row[j] += row[j - 1]
        
        for left_col in range(cols):
            for right_col in range(left_col, cols):
                cumulative_sum = 0
                sum_count = defaultdict(int)
                sum_count[0] = 1
                
                for row in matrix:
                    cumulative_sum += row[right_col] - (row[left_col - 1] if left_col > 0 else 0)
                    
                    if cumulative_sum - target in sum_count:
                        count += sum_count[cumulative_sum - target]
                    
                    sum_count[cumulative_sum] += 1
        
        return count