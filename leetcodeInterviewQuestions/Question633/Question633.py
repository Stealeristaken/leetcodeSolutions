class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        first = 0
        last = int(math.sqrt(c))
        while first <= last:
            current_sum = first ** 2 + last ** 2
            if current_sum == c:
                return True
            if c < current_sum:
                last -= 1
            else:
                first += 1
        return False