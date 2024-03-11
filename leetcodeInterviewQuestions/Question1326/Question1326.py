class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        N = len(ranges)
        stack = [0]  # Initialize a stack with the first interval
        R = 0 + ranges[0]  # Initialize R with the range of the first interval

        for i in range(1, N):
            if R >= n:
                return len(stack)
            if i + ranges[i] <= R:  # The interval is already covered
                continue
            elif i - ranges[i] <= R:  # The interval can be added
                topR = R
                while stack and stack[-1] >= i - ranges[i]:
                    topR = stack[-1]  # Update the end point
                    stack.pop()  # Remove intervals that can be covered by the new interval
                stack.append(topR)  # Add the interval that is really needed
                R = i + ranges[i]  # Update R

        return len(stack) if R >= n else -1