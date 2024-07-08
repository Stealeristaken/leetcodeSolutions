class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [_ + 1 for _ in range(n)]
        last = 0
        while n != 1:
            last = ((last + k - 1) + n) % n
            del friends[last]
            n -= 1
        return friends[-1]



########################### JOJO FLOW THE WIND ################################


from collections import deque


class Solution:

    def findTheWinner(self, n: int, k: int) -> int:
        d = deque(x for x in range(1, n + 1))
        while len(d) > 1:
            for x in range(k - 1):
                d.append(d.popleft())
            d.popleft()
        return d[0]


if __name__ == '__main__':
    sol = Solution()
    n = 10
    k = 3
    print(sol.findTheWinner(n, k))