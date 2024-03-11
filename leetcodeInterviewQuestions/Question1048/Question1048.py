class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        d = defaultdict(int)
        for word in sorted(words, key=len):
            n, d[word] = len(word), 1

            for i in range(n):
                w = word[:i] + word[i + 1:]

                if w in d:
                    d[word] = max(d[word], d[w] + 1)

        return max(d.values())