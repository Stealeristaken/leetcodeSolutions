class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        removed = set()
        res = 0
        while stones:
            row,col = stones.pop()
            if (row,col) in removed:
                continue
            stack = [(row,col)]
            count = 0
            while stack:
                cr, cc = stack.pop()
                count += 1
                for r,c in stones:
                    if (r,c) not in removed and (r == cr or c == cc):
                        stack.append((r,c))
                        removed.add((r,c))
            res += count-1
        return res
            