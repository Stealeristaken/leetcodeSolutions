class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        nums = list(chain.from_iterable(matrix))
        best = sum(abs(x) for x in nums)
        cnt = sum(x < 0 for x in nums)
        return best - (min(2 * abs(n) for n in nums) if cnt % 2 else 0)