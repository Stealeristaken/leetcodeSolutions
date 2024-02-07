from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        k = Counter(s)
        k4 = ''
        sorted_chars = sorted(k, key=lambda x: (-k[x], x))
        for char in sorted_chars:
            k4 += char * k[char]

        return k4