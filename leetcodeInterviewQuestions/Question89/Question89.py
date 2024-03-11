class Solution:
    def grayCode(self, n: int) -> List[int]:
        graySeq = [0]

        for i in range(n):
            size = 2 ** i
            reversedSeq = graySeq[::-1]
            graySeq += [num + size for num in reversedSeq]
        return graySeq
