class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        c1 = Counter(word1)
        c2 = Counter(word2)

        v1 = sorted(c1.values())
        v2 = sorted(c2.values())

        k1 = c1.keys()
        k2 = c2.keys()
        return v1 == v2 and k1 == k2