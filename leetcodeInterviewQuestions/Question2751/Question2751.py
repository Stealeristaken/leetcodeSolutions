class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        items = sorted(zip(positions, healths, directions, range(len(positions))))
        left, right = [], []
        for p, h, d, i in items:
            if d == 'L':
                while left and h > 0:
                    if h > left[-1][1]:
                        left.pop()
                        h -= 1
                    else:
                        if left[-1][1] > h:
                            left[-1][1] -= 1
                        else:
                            left.pop()
                        h = 0
                if h > 0:
                    right.append([i, h])
            else:
                left.append([i, h])
        return [h for i, h in sorted(left + right)]