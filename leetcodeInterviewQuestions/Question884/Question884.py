from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        sentence1 = s1.split(' ')
        sentence2 = s2.split(' ')
        freq = {}
        sentence = sentence1 + sentence2
        for word in sentence:
            if word not in freq.keys():
                freq[word] = 1

            else :
                freq[word] += 1

        uncommon_words = []
        for key, value in freq.items():
            if freq[key] == 1:
                uncommon_words.append(key)
        return uncommon_words