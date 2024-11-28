class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # All possible adjacents cells are up, down, left, right
        edges = [(-1,0), (1,0), (0,-1), (0,1)]
        
        # Build a graph where each cell is a node and edges are weighted adjacents cells.
        # (row, clmn): [(weight, obstacles, row, clmn)]
        graph = defaultdict(List[List[int]])

        m,n = len(grid), len(grid[0])

        for r in range(m):
            for c in range(n):
                # Explore all edges
                for edge in edges:
                    # Build the adjacent cell
                    next_row, next_clmn = r + edge[0], c + edge[1]

                    # Skip invalid edge
                    if next_row < 0 or\
                        next_row >= m or\
                        next_clmn < 0 or\
                        next_clmn >= n:
                        continue

                    # Build the graph
                    if (r,c) not in graph:
                        graph[(r,c)] = []

                    # (weight, obstacles, row_0, clmn_0)
                    graph[(r,c)].append([
                        grid[next_row][next_clmn], \
                        grid[next_row][next_clmn], \
                        next_row, \
                        next_clmn
                    ])

        # Dijkstra's Algorithm
        # Create a priority queue from start cell 
        # (weight, obstacles, row_0, clmn_0)
        queue = [(grid[0][0],0,0,0)]
        heapq.heapify(queue)
        visited = set((0,0))

        while queue:
            for _ in range(len(queue)):
                weight, obstacles, row, clmn = heapq.heappop(queue)
                
                # Reach the target
                if row == m - 1 \
                and clmn == n - 1:
                    return obstacles

                for adj_w, adj_obstacles, adj_row, adj_clmn in graph[(row,clmn)]:
                    # Skip already visited node
                    if (adj_row, adj_clmn) in visited:
                        continue

                    # Push next node updating obstacles count
                    heapq.heappush(queue, \
                        (
                            adj_w, \
                            adj_obstacles + obstacles,\
                            adj_row, adj_clmn
                        )
                    )

                    # Mark as visited
                    visited.add((adj_row, adj_clmn))
        
        # Never reach this point
        return -1