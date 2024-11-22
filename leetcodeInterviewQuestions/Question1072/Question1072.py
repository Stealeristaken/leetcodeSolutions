class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = defaultdict(int)

        for row in matrix:
            # Represent the row as a pattern relative to the first element
            base_pattern = tuple(x ^ row[0] for x in row)
            patterns[base_pattern] += 1

        return max(patterns.values())