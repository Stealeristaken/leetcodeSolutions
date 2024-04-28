from typing import List
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        res = [0] * n
        q = list(range(n))
        for i in deck:
            res[q.pop(0)] = i
            if q:
                q.append(q.pop(0))
        return res