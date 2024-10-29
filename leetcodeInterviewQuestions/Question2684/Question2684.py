class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        answer = 0
        dic = {}

        def dfs(x,y,curNum):
            if x < 0 or x == rows or y < 0 or y == cols or grid[x][y] <= curNum:
                return 0

            newNum = grid[x][y]

            if (x,y) in dic:
                return dic[(x,y)]

            first = dfs(x-1,y+1,newNum)
            second = dfs(x, y+1, newNum)
            third = dfs(x+1,y+1,newNum)

            dic[(x,y)] = 1 + max(first, second, third)
            return dic[(x,y)]
        
        for row in range(rows):
            answer = max(dfs(row, 0, 0), answer)
        
        return answer - 1
        