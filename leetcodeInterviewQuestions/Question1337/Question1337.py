class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        indexMat = [(sum(row), i) for i, row in enumerate(mat)]
        indexMat = sorted(indexMat, key=lambda i: (i[0], i[1]))

        return [i[1] for i in indexMat[:k]]