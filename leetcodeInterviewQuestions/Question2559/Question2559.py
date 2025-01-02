from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels={'a','e','i','o','u'}
        prefix = [0] * n
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i] = prefix[i - 1] + 1 if i > 0 else 1
            else:
                prefix[i] = prefix[i - 1] if i > 0 else 0
        ans = []
        for s, e in queries:
            ans.append(prefix[e] - (prefix[s-1] if s>0 else 0))
        return ans