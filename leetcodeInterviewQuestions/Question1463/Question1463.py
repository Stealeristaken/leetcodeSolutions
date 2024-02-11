class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row , col = len(grid), len(grid[0])

        prev_dp = [[0] * col for _ in range(col)]

        for r in reversed(range(row)):
            curr_dp = [[0] * col for _ in range(col)]
            for c1 in range(col - 1):
                for c2 in range(c1 + 1, col):
                    max_cher = 0
                    cher = grid[r][c1] + grid[r][c2]
                    for c1w in [-1, 0, 1]:
                        for c2w in [-1, 0, 1]:
                            c1p = c1 + c1w
                            c2p = c2 + c2w
                            if c1p < 0 or c2p == col:
                                continue
                            max_cher = max(max_cher, prev_dp[c1p][c2p])
                    curr_dp[c1][c2] = max_cher + cher
            prev_dp = curr_dp
        return prev_dp[0][col - 1]