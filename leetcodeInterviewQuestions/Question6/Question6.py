class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        cycle_length = 2 * (numRows - 1)
        result_rows = [""] * numRows

        apply_to_result = lambda i, row: result_rows.__setitem__(row, result_rows[row] + s[i])

        for i, c in enumerate(s):
            row = i % cycle_length
            row = cycle_length - row if row >= numRows else row
            apply_to_result(i, row)

        return "".join(result_rows)
