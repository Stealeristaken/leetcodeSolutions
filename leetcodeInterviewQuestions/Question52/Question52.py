class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0

        # node = (taken columns, taken positive diagonals, taken negative diagonals, row to explore)
        queen = [(set(), set(), set(), 0)]
        while queen:
            columns, posDiagram, negDiagram, row = queen.pop()

            # end case: we've successfully added n queens if next row is out of bond.
            # Otherwise we'd stop earlier
            if row == n:
                result += 1
                continue

            # try to add new queen
            for column in range(n):
                # if column or either diagonal is busy, skip
                if column in columns or column - row in posDiagram or column + row in negDiagram:
                    continue
                # otherwise add new queen: update the busy columns and diagonals
                queen.append((columns | {column}, posDiagram | {column - row}, negDiagram | {column + row}, row + 1))

        return result