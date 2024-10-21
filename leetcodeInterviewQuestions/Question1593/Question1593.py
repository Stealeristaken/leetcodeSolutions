class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()

        def backtrack(start):
            maxPart = int(s[start:] not in seen)

            for i in range(start + 1, len(s)):
                part1 = s[start:i]
                if part1 not in seen:
                    seen.add(part1)

                    parts = backtrack(i)
                    maxPart = max(maxPart, parts + 1)

                    seen.remove(part1)

            return maxPart

        return backtrack(0)