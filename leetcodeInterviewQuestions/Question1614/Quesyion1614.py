class Solution():
    def maxDepth(self, s: str) -> int:
        return max(accumulate(s, lambda s, d: s + (1 if d == "(" else (-1 if d == ')' else 0)), initial=0))