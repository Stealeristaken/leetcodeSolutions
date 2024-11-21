class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        blocked = set((r, c) for r, c in guards + walls)  
        guarded = set()  
        for r, c in guards:
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Check all 4 directions
                x, y = r + dr, c + dc
                while 0 <= x < m and 0 <= y < n and (x, y) not in blocked:
                    if (x, y) not in guarded:
                        guarded.add((x, y))
                    x, y = x + dr, y + dc
        total_cells = m * n  
        occupied = len(blocked)  
        unguarded = total_cells - len(guarded) - occupied  
        return unguarded