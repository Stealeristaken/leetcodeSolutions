from collections import defaultdict, deque
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Build graph for rows and columns
        row_graph = defaultdict(list)
        col_graph = defaultdict(list)
        row_in_degree = [0] * (k + 1)
        col_in_degree = [0] * (k + 1)
        
        for above, below in rowConditions:
            row_graph[above].append(below)
            row_in_degree[below] += 1
            
        for left, right in colConditions:
            col_graph[left].append(right)
            col_in_degree[right] += 1
            
        # Topological sorting for rows and columns
        row_queue = deque([i for i in range(1, k + 1) if row_in_degree[i] == 0])
        col_queue = deque([i for i in range(1, k + 1) if col_in_degree[i] == 0])
        
        row_order = []
        col_order = []
        
        while row_queue:
            node = row_queue.popleft()
            row_order.append(node)
            for neighbor in row_graph[node]:
                row_in_degree[neighbor] -= 1
                if row_in_degree[neighbor] == 0:
                    row_queue.append(neighbor)
                    
        while col_queue:
            node = col_queue.popleft()
            col_order.append(node)
            for neighbor in col_graph[node]:
                col_in_degree[neighbor] -= 1
                if col_in_degree[neighbor] == 0:
                    col_queue.append(neighbor)
                    
        # If there is a cycle, return an empty matrix
        if len(row_order) != k or len(col_order) != k:
            return []
        
        # Build the matrix
        matrix = [[0] * k for _ in range(k)]
        for i, num in enumerate(row_order):
            for j, col_num in enumerate(col_order):
                if num == col_num:
                    matrix[i][j] = num
        return matrix