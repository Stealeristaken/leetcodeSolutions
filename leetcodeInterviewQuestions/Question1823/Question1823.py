class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [_ + 1 for _ in range(n)]
        last = 0
        while n != 1:
            last = ((last + k - 1) + n) % n
            del friends[last]
            n -= 1
        return friends[-1]
