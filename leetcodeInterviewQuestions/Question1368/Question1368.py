class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        PATHS = ((0, 1, 1), (0, -1, 2), (1, 0, 3), (-1, 0, 4))
        queue = deque([(0, 0, 0)])
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        while queue:
            x, y, cost = queue.popleft()

            if (x, y) == (m - 1, n - 1):
                return cost

            if visited[x][y]:
                continue

            visited[x][y] = True

            for dx, dy, di in PATHS:
                xx, yy = x + dx, y + dy

                if 0 <= xx < m and 0 <= yy < n and not visited[xx][yy]:
                    if grid[x][y] == di:
                        queue.appendleft((xx, yy, cost))
                    else:
                        queue.append((xx, yy, cost + 1))