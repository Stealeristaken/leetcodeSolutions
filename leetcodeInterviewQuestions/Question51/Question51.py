class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        columns = set()
        posDiagram = set()  # (r+c)
        negDiagram = set()  # (r-c)

        res = []

        board = [['.'] * n for i in range(n)]

        def backtrack(r):
            # base case
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):

                if c in columns or (r + c) in posDiagram or (r - c) in negDiagram:
                    continue

                columns.add(c)
                posDiagram.add(r + c)
                negDiagram.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                columns.remove(c)
                posDiagram.remove(r + c)
                negDiagram.remove(r - c)
                board[r][c] = '.'

        backtrack(0)
        return res