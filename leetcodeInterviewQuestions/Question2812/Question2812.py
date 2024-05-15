import heapq
from typing import List
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def compute_grid():
            dequeue = deque()
            min_dist = {}
            for row in range(n):
                for column in range(n):
                    if grid[row][column]:
                        dequeue.append([row, column, 0])
                        min_dist[(row, column)] = 0
            
            while dequeue:
                row, column, distance = dequeue.popleft()
                next_moves = [[row+1, column], [row-1, column], [row, column+1], [row, column-1]]
                
                for row2, col2 in next_moves:
                    if ((row2, col2) not in min_dist) and (min(row2, col2)>=0 and max(row2, col2)<n):
                        min_dist[(row2, col2)] = distance+1
                        dequeue.append([row2, col2, distance+1])

            return min_dist

        min_dist = compute_grid()

        maxHeap = [(-min_dist[(0, 0)], 0, 0)]
        visit = set()
        visit.add((0, 0))
        while maxHeap:
            dist, row, col = heapq.heappop(maxHeap)
            dist = -dist
            if (row, col) == (n-1, n-1):
                return dist
            
            next_moves = [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]
            for row2, col2 in next_moves:
                if ((row2, col2) not in visit) and (max(row2, col2)<n and min(row2, col2)>=0):
                    visit.add((row2, col2))
                    dist2 = min(dist, min_dist[(row2, col2)])
                    heapq.heappush(maxHeap, (-dist2, row2, col2))