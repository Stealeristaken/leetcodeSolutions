'''
We can see that this is a recursive problem.
At every step we can make 2 moves, right or down.
If we move down, we decrease the row by 1, and if we move right, we decrease the column by 1.
We can make these steps in an m x n grid.
So the time complexity for a normal recursive function will be O(2^(m+n)) which is very high.
We can use a dictionary to store the result of our recursive calls at each step,
and if we ever get the same input in a future call,
we can access it directly from the dictionary instead of making repetitive recursive calls.
'''


class Solution:
    def uniquePaths(self, m: int, n: int, memo = {}) -> int:
        # We use a dictionary called memo to store all results
        # If our current (m,n) are already in memo then
        # We don't call recursively again, we just extract from memo

        # If we try dry running, we'll realize that (m,n) and (n,m)
        # will give same result recursively, so we can use them interchangeably
        if (m,n) in memo: return memo[(m,n)]
        if (n,m) in memo: return memo[(n,m)]

        # Base cases
        if (m == 1 and n == 1): return 1
        if (m == 0 or n == 0): return 0

        # Recursively calling the function and storing the result in memo
        memo[(m,n)] = self.uniquePaths(m-1,n, memo) + self.uniquePaths(m,n-1, memo)

        return memo[(m,n)]
