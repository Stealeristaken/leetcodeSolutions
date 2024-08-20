class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)
        
        @cache
        def stoneGame(index: int, M: int) -> int:

            total = sum(piles[index:])
            if index + 2 * M >= n:
                return total
            
            max_score = 0
            for X in range(1, 2 * M + 1):
                new_M = max(M, X)
                score = total - stoneGame(index + X, new_M)
                if score > max_score:
                    max_score = score
            
            return max_score
        
        return stoneGame(0, 1)